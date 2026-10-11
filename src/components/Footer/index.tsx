import { FaArrowUp, FaGithub, FaLinkedin } from 'react-icons/fa'

export default function Footer() {
  return (
    <footer className="border-t border-white/10 bg-slate-950/80 py-8">
      <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 px-4 text-sm md:flex-row md:px-6">
        <p className="text-slate-300">
          © {new Date().getFullYear()} Aung Myat Min. All rights reserved.
        </p>

        <div className="flex items-center gap-3 text-lg text-slate-300">
          <a
            aria-label="GitHub profile"
            href="https://github.com/Moonlight-22"
            target="_blank"
            rel="noreferrer"
            className="flex h-10 w-10 items-center justify-center rounded-full transition hover:-translate-y-0.5 hover:bg-violet-500/10 hover:text-violet-300"
          >
            <FaGithub />
          </a>
          <a
            aria-label="LinkedIn profile"
            href="https://www.linkedin.com/in/aung-min-a581a7307/ "
            target="_blank"
            rel="noreferrer"
            className="flex h-10 w-10 items-center justify-center rounded-full transition hover:-translate-y-0.5 hover:bg-violet-500/10 hover:text-violet-300"
          >
            <FaLinkedin />
          </a>
          <a
            aria-label="Back to top"
            href="#home"
            className="flex h-10 w-10 items-center justify-center rounded-full transition hover:-translate-y-0.5 hover:bg-violet-500/10 hover:text-violet-300"
          >
            <FaArrowUp />
          </a>
        </div>
      </div>
    </footer>
  )
}
