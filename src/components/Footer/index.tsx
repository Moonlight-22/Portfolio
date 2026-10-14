import { useEffect, useState } from 'react'
import { FaGithub, FaLinkedin } from 'react-icons/fa'
import { FaHouse, FaUser, FaFolderOpen, FaCertificate, FaEnvelope } from 'react-icons/fa6'
import { SiGmail } from 'react-icons/si'

const mobileLinks = [
  { label: 'Home', href: '/#home', icon: FaHouse },
  { label: 'About', href: '/#about', icon: FaUser },
  { label: 'Projects', href: '/#projects', icon: FaFolderOpen },
  { label: 'Certificates', href: '/#certificates', icon: FaCertificate },
  { label: 'Contact', href: '/#contact', icon: FaEnvelope },
]

export default function Footer() {
  const [activeSection, setActiveSection] = useState<string | null>(null)

  useEffect(() => {
    const updateActiveSection = () => {
      const marker = window.scrollY + window.innerHeight * 0.4
      const currentSection = mobileLinks.find(({ href }) => {
        const section = document.getElementById(href.slice(2))
        return section
          ? marker >= section.offsetTop && marker < section.offsetTop + section.offsetHeight
          : false
      })
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

  return (
    <>
      <footer className="border-t border-white/10 bg-[#080a0d]/90 py-8">
        <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 px-4 text-xs md:flex-row md:px-6 md:text-sm">
          <p className="text-center text-slate-300">
            © {new Date().getFullYear()} Aung Myat Min. All rights reserved.
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
        className="fixed inset-x-0 bottom-0 z-40 border-t border-white/10 bg-[#080a0d]/95 px-2 pb-[max(env(safe-area-inset-bottom),0.5rem)] pt-2 shadow-[0_-12px_40px_rgba(0,0,0,0.55)] backdrop-blur-xl md:hidden"
      >
        <div className="mx-auto flex max-w-md items-center justify-around">
          {mobileLinks.map(({ label, href, icon: Icon }) => (
            <a
              key={href}
              href={href}
              aria-label={label}
              aria-current={activeSection === href ? 'location' : undefined}
              className={`flex min-w-12 touch-manipulation flex-col items-center gap-1 rounded-xl px-2 py-1.5 transition duration-150 hover:-translate-y-0.5 hover:bg-sky-500/10 hover:text-sky-300 active:scale-90 active:bg-sky-500/25 active:text-sky-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-sky-400/70 ${
                activeSection === href
                  ? 'bg-sky-500/10 text-sky-300'
                  : 'text-slate-400'
              }`}
            >
              <Icon aria-hidden="true" className="text-base" />
              <span className="text-[10px] font-medium">{label}</span>
            </a>
          ))}
        </div>
      </nav>
    </>
  )
}
