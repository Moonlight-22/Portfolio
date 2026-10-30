import ProfileImage from '../../assets/images/Profile_photo.jpg'
import cv from '../../assets/file/Aung_Myat_Min_CV.pdf'
import { motion } from 'framer-motion'

export default function Hero() {
  return (
    <section id="home" className="mx-auto grid min-h-[calc(100svh-4rem)] max-w-6xl items-center gap-8 overflow-hidden px-4 py-10 md:grid-cols-[1.1fr_0.9fr] md:px-6 md:py-14">
      <motion.div
        initial={{ opacity: 0, x: -24 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.7 }}
        className="relative z-10 order-1 text-left md:order-1"
      >
        <h1 className="text-4xl font-black leading-[1.05] tracking-tight text-white sm:text-5xl md:text-6xl lg:text-7xl">
          Aung Myat Min
        </h1>
        <h2 className="mt-2 text-3xl font-normal leading-tight tracking-tight text-slate-100 sm:text-4xl md:text-5xl">
          <span>IT Support &</span>
          <br className="sm:hidden" />{' '}
          <span className="font-bold text-sky-400">Full-Stack Developer</span>
        </h2>
        <div className="mt-5 flex flex-wrap items-center gap-x-3 gap-y-2 text-sm font-semibold text-slate-300 sm:text-base">
          <span>Technical Support</span>
          <span aria-hidden="true" className="text-slate-600">•</span>
          <span>Web Development</span>
          <span aria-hidden="true" className="text-slate-600">•</span>
          <span>Problem Solving</span>
        </div>
        <p className="mt-5 max-w-xl text-justify text-sm leading-6 text-slate-400 sm:text-base sm:leading-7">
          I support users and build thoughtful digital experiences with modern web technologies, combining practical
          troubleshooting with a focus on clear, reliable design.
        </p>
        <div className="mt-7 flex flex-wrap gap-4">
          <a
            href={cv}
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center justify-center rounded-md border border-sky-600 bg-sky-600 px-6 py-3 text-sm font-semibold text-white shadow-md shadow-black/20 transition-all duration-200 hover:-translate-y-0.5 hover:border-sky-500 hover:bg-sky-500 hover:shadow-[0_0_28px_rgba(96,165,250,0.45)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-sky-400"
          >
            VIEW CV
          </a>
          <a
            href="#contact"
            className="rounded-md border border-slate-500 px-6 py-3 text-sm font-bold text-slate-200 transition-colors hover:bg-slate-800"
          >
            Contact Me
          </a>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, x: 24 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ delay: 0.2, duration: 0.7 }}
        className="relative order-2 mx-auto aspect-[768/1309] w-[13rem] sm:w-[15rem] md:order-2 md:w-[18rem]"
      >
        <div className="relative h-full w-full">
          <img
            src={ProfileImage}
            alt="Aung Myat Min"
            className="h-full w-full object-contain object-center shadow-[0_0_18px_rgba(148,163,184,0.28)]"
          />
        </div>
      </motion.div>
    </section>
  )
}
