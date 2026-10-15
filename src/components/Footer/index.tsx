import { useEffect, useState } from 'react'
import { FaGithub, FaLinkedin } from 'react-icons/fa'
import {
  FaBrain,
  FaCertificate,
  FaEnvelope,
  FaFolderOpen,
  FaGrip,
  FaHouse,
  FaUser,
  FaXmark,
} from 'react-icons/fa6'
import { SiGmail } from 'react-icons/si'

const mobileLinks = [
  { label: 'Home', href: '/#home', icon: FaHouse },
  { label: 'About', href: '/#about', icon: FaUser },
  { label: 'Skills', href: '/#skills', icon: FaBrain },
  { label: 'Projects', href: '/#projects', icon: FaFolderOpen },
  { label: 'Certificates', href: '/#certificates', icon: FaCertificate },
  { label: 'Contact', href: '/#contact', icon: FaEnvelope },
]

const visibleLinks = [mobileLinks[0], mobileLinks[1], mobileLinks[3], mobileLinks[5]]
const hiddenLinks = [mobileLinks[2], mobileLinks[4]]

export default function Footer() {
  const [activeSection, setActiveSection] = useState<string | null>(null)
  const [menuOpen, setMenuOpen] = useState(false)

  useEffect(() => {
    const updateActiveSection = () => {
      const marker = Math.min(window.innerHeight * 0.35, 180)
      let currentSection: (typeof mobileLinks)[number] | null = mobileLinks[0]

      for (const link of mobileLinks) {
        const section = document.getElementById(link.href.slice(2))
        if (section && section.getBoundingClientRect().top <= marker) {
          currentSection = link
        }
      }

      const isAtPageBottom =
        window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2
      if (isAtPageBottom) currentSection = mobileLinks[mobileLinks.length - 1]

      setActiveSection(currentSection?.href ?? null)
    }

    updateActiveSection()
    window.addEventListener('scroll', updateActiveSection, { passive: true })
    window.addEventListener('resize', updateActiveSection)
    return () => {
      window.removeEventListener('scroll', updateActiveSection)
      window.removeEventListener('resize', updateActiveSection)
    }
  }, [])

  useEffect(() => {
    if (!menuOpen) return

    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setMenuOpen(false)
    }
    window.addEventListener('keydown', closeOnEscape)
    return () => window.removeEventListener('keydown', closeOnEscape)
  }, [menuOpen])

  return (
    <>
      <footer className="border-t border-white/10 bg-[#080a0d]/90 py-8">
        <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 px-4 text-xs md:flex-row md:px-6 md:text-sm">
          <p className="text-center text-slate-300">
            © {new Date().getFullYear()} Aung Myat Min Portfolio.
          </p>

          <div className="flex items-center gap-3 text-lg text-slate-300">
            <a
              aria-label="GitHub profile"
              href="https://github.com/Moonlight-22"
              target="_blank"
              rel="noreferrer"
              className="flex h-10 w-10 items-center justify-center rounded-full transition hover:-translate-y-0.5 hover:bg-sky-500/10 hover:text-sky-300"
            >
              <FaGithub />
            </a>
            <a
              aria-label="LinkedIn profile"
              href="https://www.linkedin.com/in/aung-min-a581a7307/"
              target="_blank"
              rel="noreferrer"
              className="flex h-10 w-10 items-center justify-center rounded-full transition hover:-translate-y-0.5 hover:bg-sky-500/10 hover:text-sky-300"
            >
              <FaLinkedin />
            </a>
            <a
              aria-label="Email Aung Myat Min"
              href="mailto:aungmyatmin984@gmail.com"
              className="flex h-10 w-10 items-center justify-center rounded-full transition hover:-translate-y-0.5 hover:bg-sky-500/10 hover:text-sky-300"
            >
              <SiGmail />
            </a>
          </div>
        </div>
      </footer>
      <nav
        aria-label="Mobile footer navigation"
        className="fixed inset-x-0 bottom-0 z-40 border-t border-white/10 bg-[#080a0d]/95 px-2 pb-[max(env(safe-area-inset-bottom),0.5rem)] pt-2 shadow-[0_-12px_40px_rgba(0,0,0,0.45)] backdrop-blur-xl md:hidden"
      >
        <div className="mx-auto grid max-w-lg grid-cols-5 items-end">
          {visibleLinks.slice(0, 2).map(({ label, href, icon: Icon }) => (
            <a
              key={href}
              href={href}
              aria-current={activeSection === href ? 'location' : undefined}
              className={`flex min-w-0 flex-col items-center gap-1 rounded-xl px-1 py-2 text-[10px] font-medium transition-colors hover:text-sky-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-400/70 ${
                activeSection === href ? 'text-sky-300' : 'text-slate-400'
              }`}
            >
              <Icon aria-hidden="true" className="text-lg" />
              <span className="truncate">{label}</span>
            </a>
          ))}
          <div className="relative">
            {menuOpen && (
              <div
                id="mobile-footer-menu"
                className="absolute bottom-[calc(100%+0.75rem)] left-1/2 grid w-[min(13rem,calc(100vw-2rem))] -translate-x-1/2 grid-cols-2 gap-2 rounded-2xl border border-white/10 bg-[#101318]/95 p-3 shadow-2xl shadow-black/50 backdrop-blur-xl"
              >
                {hiddenLinks.map(({ label, href, icon: Icon }) => (
                  <a
                    key={href}
                    href={href}
                    aria-current={activeSection === href ? 'location' : undefined}
                    onClick={() => setMenuOpen(false)}
                    className={`flex min-h-16 flex-col items-center justify-center gap-1.5 rounded-xl px-1 py-2 text-[11px] font-medium transition-colors hover:bg-white/5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-400/70 ${
                      activeSection === href ? 'text-sky-300' : 'text-slate-300'
                    }`}
                  >
                    <Icon aria-hidden="true" className="text-base" />
                    <span>{label}</span>
                  </a>
                ))}
              </div>
            )}
            <button
              type="button"
              aria-expanded={menuOpen}
              aria-controls={menuOpen ? 'mobile-footer-menu' : undefined}
              aria-label={menuOpen ? 'Close extra navigation links' : 'Show Skills and Certificates'}
              onClick={() => setMenuOpen((open) => !open)}
              className="relative -mt-6 flex h-14 w-14 justify-self-center items-center justify-center rounded-full border-4 border-[#080a0d] bg-sky-600 text-lg text-white shadow-lg shadow-sky-950/50 transition-colors hover:bg-sky-500 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-300"
            >
              {menuOpen ? <FaXmark aria-hidden="true" /> : <FaGrip aria-hidden="true" />}
            </button>
          </div>
          {visibleLinks.slice(2).map(({ label, href, icon: Icon }) => (
            <a
              key={href}
              href={href}
              aria-current={activeSection === href ? 'location' : undefined}
              className={`flex min-w-0 flex-col items-center gap-1 rounded-xl px-1 py-2 text-[10px] font-medium transition-colors hover:text-sky-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-400/70 ${
                activeSection === href ? 'text-sky-300' : 'text-slate-400'
              }`}
            >
              <Icon aria-hidden="true" className="text-lg" />
              <span className="truncate">{label}</span>
            </a>
          ))}
        </div>
      </nav>
    </>
  )
}
