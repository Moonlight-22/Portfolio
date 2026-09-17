import { FaArrowUp, FaEnvelope, FaGithub, FaLinkedin } from 'react-icons/fa'

export default function Footer() {
  return (
    <footer className="border-t border-slate-200 bg-white/70 py-8 dark:border-slate-800 dark:bg-slate-950/80">
      <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 px-4 text-sm md:flex-row md:px-6">
        <p className="text-slate-600 dark:text-slate-300">
          © {new Date().getFullYear()} Your Name. All rights reserved.
        </p>

        <div className="flex items-center gap-3 text-lg">
          <a aria-label="GitHub profile" href="https://github.com/" target="_blank" rel="noreferrer">
            <FaGithub />
          </a>
          <a aria-label="LinkedIn profile" href="https://linkedin.com/" target="_blank" rel="noreferrer">
            <FaLinkedin />
          </a>
          <a aria-label="Send email" href="mailto:you@example.com">
            <FaEnvelope />
          </a>
          <a aria-label="Back to top" href="#home">
            <FaArrowUp />
          </a>
        </div>
      </div>
    </footer>
  )
}
