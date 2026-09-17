import ProfileImage from '../../assets/images/Profile_pic.png'
import cv from '../../assets/file/Aung_Myat_Min_CV.pdf-1.pdf'
import { motion } from 'framer-motion'
import { FaDownload, FaGithub, FaLinkedin } from 'react-icons/fa'

export default function Hero() {
  return (
    <section id="home" className="mx-auto grid max-w-6xl gap-10 px-4 pb-16 pt-14 md:grid-cols-2 md:px-6 md:pt-20">
      <motion.div initial={{ opacity: 0, y: 24 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.7 }}>
        <p className="mb-4 text-sm font-semibold uppercase tracking-[0.25em] text--100">IT SUPPORT & GRAPHIC DESIGN</p>
        <h1 className="text-4xl font-black leading-tight md:text-6xl">
          Building premium <span className="text-violet-600">web experiences</span>.
        </h1>
        <p className="mt-5 max-w-xl text-slate-600 dark:text-slate-300">
          I create clean, responsive, and high-performance applications with modern frontend architecture and thoughtful
          user experience.
        </p>

        <div className="mt-8 flex flex-wrap gap-3">
          <a href={cv} download className="rounded-full bg-violet-600 px-6 py-3 font-semibold text-white hover:bg-violet-500">
            <span className="inline-flex items-center gap-2" >
              <FaDownload /> Download CV
            </span>
          </a>
          <a
            href="#projects"
            className="rounded-full border border-slate-300 px-6 py-3 font-semibold hover:bg-slate-100 dark:border-slate-700 dark:hover:bg-slate-800"
          >
            View Projects
          </a>
        </div>

        <div className="mt-8 flex gap-4 text-2xl text-slate-700 dark:text-slate-200">
          <a aria-label="GitHub profile" href="https://github.com/Moonlight-22" target="_blank" rel="noreferrer">
            <FaGithub />
          </a>
          <a aria-label="LinkedIn profile" href="https://www.linkedin.com/in/aung-min-a581a7307/" target="_blank" rel="noreferrer">
            <FaLinkedin />
          </a>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 0.2, duration: 0.7 }}
        className="relative mx-auto flex h-72 w-72 items-center justify-center rounded-[1rem] boder-2 border-slate-200 bg-slate-100 shadow-lg dark:border-slate-700 dark:bg-slate-800 md:h-96 md:w-96 p-2"
      >
        <div className=" glass flex h-full w-full items-center justify-center boder border-slate-200 bg-slate-100 shadow-lg rounded-[1rem] ">
          <img src={ProfileImage} alt="Profile" className="h-full w-full rounded-[1rem] object-cover" />
        </div>
      </motion.div>
    </section>
  )
}
