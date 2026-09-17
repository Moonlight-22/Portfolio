import { useEffect, useMemo, useState } from 'react'
import { FaBars, FaTimes } from 'react-icons/fa'
import ThemeToggle from '../ThemeToggle'

const links = [
  { label: 'Home', href: '#home' },
  { label: 'About', href: '#about' },
  { label: 'Skills', href: '#skills' },
  { label: 'Projects', href: '#projects' },
  { label: 'Certificates', href: '#certificates' },
  { label: 'Contact', href: '#contact' },
]

export default function Navbar() {
  const [open, setOpen] = useState(false)
  const [active, setActive] = useState('home')
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    const onScroll = () => {
      const sections = links
        .map((link) => document.querySelector(link.href))
        .filter(Boolean) as HTMLElement[]
      const y = window.scrollY + 120
      for (const section of sections) {
        if (y >= section.offsetTop && y < section.offsetTop + section.offsetHeight) {
          setActive(section.id)
        }
      }
      const max = document.documentElement.scrollHeight - window.innerHeight
      setProgress(max > 0 ? (window.scrollY / max) * 100 : 0)
    }
    onScroll()
    window.addEventListener('scroll', onScroll)
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  const navItems = useMemo(
    () =>
      links.map((link) => (
        <a
          key={link.href}
          href={link.href}
          onClick={() => setOpen(false)}
          className={`rounded-full px-4 py-2 text-sm transition ${
            active === link.href.slice(1)
              ? 'bg-violet-600 text-white'
              : 'text-slate-700 hover:bg-slate-200 dark:text-slate-200 dark:hover:bg-slate-800'
          }`}
        >
          {link.label}
        </a>
      )),
    [active],
  )

  return (
    <header className="sticky top-0 z-50 border-b border-slate-200/70 bg-white/70 backdrop-blur-xl dark:border-slate-800 dark:bg-slate-950/70">
      <div className="h-1 bg-violet-500 transition-all" style={{ width: `${progress}%` }} />
      <nav className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3 md:px-6">
        <a href="#home" className="text-lg font-bold tracking-tight">
          Portfolio
        </a>

        <div className="hidden items-center gap-2 md:flex">
          {navItems}
          <ThemeToggle />
        </div>

        <div className="flex items-center gap-2 md:hidden">
          <ThemeToggle />
          <button
            type="button"
            onClick={() => setOpen((prev) => !prev)}
            className="rounded-md border border-slate-300 p-2 dark:border-slate-700"
            aria-label="Toggle mobile menu"
            aria-expanded={open}
          >
            {open ? <FaTimes /> : <FaBars />}
          </button>
        </div>
      </nav>

      {open ? <div className="flex flex-col gap-2 border-t border-slate-200 px-4 py-4 md:hidden dark:border-slate-800">{navItems}</div> : null}
    </header>
  )
}
