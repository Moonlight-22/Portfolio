import { useEffect, useMemo, useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { FaBars, FaTimes } from 'react-icons/fa'

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

  useEffect(() => {
    if (!open) return

    const previousOverflow = document.body.style.overflow
    document.body.style.overflow = 'hidden'

    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setOpen(false)
    }

    window.addEventListener('keydown', onKeyDown)
    return () => {
      document.body.style.overflow = previousOverflow
      window.removeEventListener('keydown', onKeyDown)
    }
  }, [open])

  const navItems = useMemo(
    () =>
      links.map((link) => (
        <a
          key={link.href}
          href={`/${link.href}`}
          onClick={() => setOpen(false)}
          className={`rounded-full px-4 py-2 text-sm font-medium transition-all duration-200 ${
            active === link.href.slice(1)
              ? 'bg-sky-600 text-white shadow-[0_0_24px_rgba(96,165,250,0.25)]'
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

          <div className="flex items-center gap-2 md:hidden">
            <button
              type="button"
              onClick={() => setOpen((prev) => !prev)}
              className="rounded-xl border border-white/10 p-2.5 text-slate-200 transition hover:border-sky-400/50 hover:bg-white/5"
              aria-label={open ? 'Close navigation menu' : 'Open navigation menu'}
              aria-expanded={open}
              aria-controls="mobile-navigation"
            >
              {open ? <FaTimes /> : <FaBars />}
            </button>
          </div>
        </nav>
      </header>

      <AnimatePresence>
        {open ? (
          <div className="fixed inset-0 z-[60] md:hidden">
            <motion.button
              type="button"
              aria-label="Close navigation menu"
              className="absolute inset-0 h-full w-full bg-black/75 backdrop-blur-sm"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.2 }}
              onClick={() => setOpen(false)}
            />
            <motion.aside
              id="mobile-navigation"
              role="dialog"
              aria-modal="true"
              aria-label="Mobile navigation"
              className="absolute inset-y-0 right-0 flex w-[min(72vw,17rem)] flex-col border-l border-white/10 bg-[#101318] shadow-2xl shadow-black/70"
              initial={{ x: '100%' }}
              animate={{ x: 0 }}
              exit={{ x: '100%' }}
              transition={{ type: 'spring', damping: 28, stiffness: 260 }}
            >
              <div className="flex items-center justify-between border-b border-white/10 px-4 py-3.5">
                <a
                  href="/#home"
                  onClick={() => setOpen(false)}
                  className="text-[13px] font-bold tracking-[0.08em] text-white"
                >
                  Portfolio
                </a>
                <button
                  type="button"
                  onClick={() => setOpen(false)}
                  className="rounded-lg border border-white/10 p-2.5 text-xs text-slate-300 transition hover:border-sky-400/50 hover:text-white"
                  aria-label="Close navigation menu"
                >
                  <FaTimes />
                </button>
              </div>
              <nav className="flex flex-1 flex-col items-stretch gap-1 px-3 py-4">
                {links.map((link) => (
                  <a
                    key={link.href}
                    href={`/${link.href}`}
                    onClick={() => setOpen(false)}
                    className={`flex min-h-10 w-full items-center rounded-lg px-3.5 text-left text-xs font-medium leading-4 transition-all duration-200 ${
                      active === link.href.slice(1)
                        ? 'bg-sky-600 text-white shadow-[0_0_24px_rgba(96,165,250,0.25)]'
                        : 'text-slate-300 hover:bg-white/5 hover:text-white'
                    }`}
                  >
                    {link.label}
                  </a>
                ))}
              </nav>
              <div className="border-t border-white/10 px-4 py-3.5 text-[8px] leading-4 tracking-[0.1em] text-slate-500">
                IT SUPPORT & WEB DEVELOPER
              </div>
            </motion.aside>
          </div>
        ) : null}
      </AnimatePresence>
    </>
  )
}
