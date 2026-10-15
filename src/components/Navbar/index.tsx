import { useEffect, useMemo, useState } from 'react'

const links = [
  { label: 'Home', href: '#home' },
  { label: 'About', href: '#about' },
  { label: 'Skills', href: '#skills' },
  { label: 'Projects', href: '#projects' },
  { label: 'Certificates', href: '#certificates' },
  { label: 'Contact', href: '#contact' },
]

export default function Navbar() {
  const [active, setActive] = useState('home')
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    const onScroll = () => {
      const marker = Math.min(window.innerHeight * 0.35, 180)
      let currentSection = links[0].href.slice(1)

      for (const link of links) {
        const section = document.getElementById(link.href.slice(1))
        if (section && section.getBoundingClientRect().top <= marker) {
          currentSection = section.id
        }
      }

      const isAtPageBottom =
        window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2
      if (isAtPageBottom) currentSection = links[links.length - 1].href.slice(1)

      setActive(currentSection)
      const max = document.documentElement.scrollHeight - window.innerHeight
      setProgress(max > 0 ? (window.scrollY / max) * 100 : 0)
    }
    onScroll()
    window.addEventListener('scroll', onScroll)
    window.addEventListener('resize', onScroll)
    return () => {
      window.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', onScroll)
    }
  }, [])

  const navItems = useMemo(
    () =>
      links.map((link) => (
        <a
          key={link.href}
          href={`/${link.href}`}
          className={`rounded-full px-4 py-2 text-sm font-medium transition-all duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-300 ${
            active === link.href.slice(1)
              ? 'bg-sky-600 text-white shadow-[0_0_24px_rgba(96,165,250,0.25)] hover:bg-sky-500 hover:shadow-[0_0_28px_rgba(96,165,250,0.45)]'
              : 'text-slate-300 hover:bg-white/5 hover:text-white'
          }`}
        >
          {link.label}
        </a>
      )),
    [active],
  )

  return (
    <>
      <header className="sticky top-0 z-50 border-b border-white/10 bg-[#080a0d]/85 backdrop-blur-xl">
        <div className="h-1 bg-gradient-to-r from-sky-600 via-blue-400 to-slate-300 transition-all duration-200" style={{ width: `${progress}%` }} />
        <nav className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3 md:px-6">
          <a href="/#home" className="text-lg font-bold tracking-[0.12em] text-white">
            Portfolio
          </a>

          <div className="hidden items-center gap-2 md:flex">
            {navItems}
          </div>
        </nav>
      </header>
    </>
  )
}
