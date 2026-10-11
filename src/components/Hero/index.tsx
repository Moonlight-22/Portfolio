import ProfileImage from '../../assets/images/Profile_pic.png'
import cv from '../../assets/file/Aung_Myat_Min_CV.pdf'
import { motion } from 'framer-motion'
import { FaDownload, FaGithub, FaLinkedin } from 'react-icons/fa'

export default function Hero() {
  return (
    <section id="home" className="mx-auto grid max-w-6xl gap-10 px-4 pb-16 pt-14 md:grid-cols-2 md:px-6 md:pt-20">
      <motion.div initial={{ opacity: 0, y: 24 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.7 }}>
        <p className="mb-4 text-sm font-semibold uppercase tracking-[0.25em] text-violet-300">IT SUPPORT and WEB DEVELOPER</p>
        <h1 className="text-4xl font-black leading-[1.05] md:text-6xl">
          Building <span className="bg-gradient-to-r from-violet-400 via-fuchsia-300 to-sky-300 bg-clip-text text-transparent">premium</span>{' '}
          digital experiences.
        </h1>
        <p className="mt-5 max-w-xl text-base leading-7 text-slate-300 md:text-lg">
          I create clean, responsive, and high-performing experiences that combine strong product thinking with thoughtful
          design and modern frontend engineering.
        </p>

        <div className="mt-8 flex flex-wrap gap-3">
          <a href={cv} download className="rounded-full bg-violet-600 px-6 py-3 font-semibold text-white shadow-[0_0_24px_rgba(168,85,247,0.45)] transition-all duration-200 hover:-translate-y-0.5 hover:bg-violet-500 hover:shadow-[0_0_30px_rgba(168,85,247,0.7)]">
            <span className="inline-flex items-center gap-2">
              <FaDownload /> Download CV
            </span>
          </a>
          <a
            href="#projects"
            className="rounded-full border border-white/15 bg-white/5 px-6 py-3 font-semibold text-slate-100 transition-all duration-200 hover:-translate-y-0.5 hover:border-violet-400/60 hover:bg-violet-500/10"
          >
            View Projects
          </a>
        </div>

        <div className="mt-8 flex gap-4 text-2xl text-slate-300">
          <a
            aria-label="GitHub profile"
            href="https://github.com/Moonlight-22"
            target="_blank"
            rel="noreferrer"
            className="rounded-full p-2 transition hover:-translate-y-0.5 hover:text-violet-300"
          >
            <FaGithub />
          </a>
          <a
            aria-label="LinkedIn profile"
            href="https://www.linkedin.com/in/aung-min-a581a7307/"
            target="_blank"
            rel="noreferrer"
            className="rounded-full p-2 transition hover:-translate-y-0.5 hover:text-violet-300"
          >
            <FaLinkedin />
          </a>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 0.2, duration: 0.7 }}
        className="relative mx-auto flex h-72 w-72 items-center justify-center rounded-[2rem] border border-violet-500/20 bg-slate-900/60 p-2 shadow-[0_0_60px_rgba(168,85,247,0.15)] md:h-96 md:w-96"
      >
        <div className="absolute inset-6 rounded-[1.7rem] border border-violet-400/20" />
        <div className="glass flex h-full w-full items-center justify-center overflow-hidden rounded-[1.6rem]">
          <img src={ProfileImage} alt="Profile" className="h-full w-full object-cover" />
        </div>
      </motion.div>
    </section>
  )
}
