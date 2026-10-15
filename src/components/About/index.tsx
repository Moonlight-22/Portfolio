import { motion } from 'framer-motion'
import Timeline from '../Timeline'
import SectionTitle from '../SectionTitle'

export default function About() {
  return (
    <section id="about" className="mx-auto max-w-6xl px-4 py-12 md:px-6 md:py-16">
      <SectionTitle eyebrow="About" title="About Me" />
      <div className="grid gap-6 md:grid-cols-2 md:gap-8">
        <motion.article initial={{ opacity: 0, y: 18 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} className="glass rounded-3xl border border-white/20 p-5 text-left shadow-lg md:p-6">
          <h3 className="text-lg font-bold md:text-xl">Biography</h3>
          <p className="mt-3 text-sm leading-6 text-slate-600 dark:text-slate-300 md:text-base md:leading-normal">
            I am a developer focused on building modern applications with clean architecture and delightful user
            interfaces. My interests span web engineering, AI-assisted products, and scalable frontend systems.
          </p>
          <h4 className="mt-5 text-base font-semibold md:text-lg">Education</h4>
          <p className="mt-2 text-sm leading-6 text-slate-600 dark:text-slate-300 md:text-base md:leading-normal">B.Sc. (Hons) in Computer Science</p>
          <h4 className="mt-5 text-base font-semibold md:text-lg">Career Objective</h4>
          <p className="mt-2 text-sm leading-6 text-slate-600 dark:text-slate-300 md:text-base md:leading-normal">
            To contribute to impactful products as a frontend/full-stack engineer while continuously improving software
            quality and user experience.
          </p>
        </motion.article>
        <motion.div initial={{ opacity: 0, y: 18 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} className="glass rounded-3xl border border-white/20 p-5 text-left shadow-lg md:p-6">
          <h3 className="mb-5 text-lg font-bold md:text-xl">Experience Timeline</h3>
          <Timeline />
        </motion.div>
      </div>
    </section>
  )
}
