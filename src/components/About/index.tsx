import { motion } from 'framer-motion'
import Timeline from '../Timeline'
import SectionTitle from '../SectionTitle'

export default function About() {
  return (
    <section id="about" className="mx-auto max-w-6xl px-4 py-16 md:px-6">
      <SectionTitle eyebrow="About" title="About Me" subtitle="A short background with education, objective, and experience path." />
      <div className="grid gap-8 md:grid-cols-2">
        <motion.article initial={{ opacity: 0, y: 18 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} className="glass rounded-3xl border border-white/20 p-6 shadow-lg">
          <h3 className="text-xl font-bold">Biography</h3>
          <p className="mt-3 text-slate-600 dark:text-slate-300">
            I am a developer focused on building modern applications with clean architecture and delightful user
            interfaces. My interests span web engineering, AI-assisted products, and scalable frontend systems.
          </p>
          <h4 className="mt-5 text-lg font-semibold">Education</h4>
          <p className="mt-2 text-slate-600 dark:text-slate-300">B.Sc. in Computer Science (Ongoing)</p>
          <h4 className="mt-5 text-lg font-semibold">Career Objective</h4>
          <p className="mt-2 text-slate-600 dark:text-slate-300">
            To contribute to impactful products as a frontend/full-stack engineer while continuously improving software
            quality and user experience.
          </p>
        </motion.article>
        <motion.div initial={{ opacity: 0, y: 18 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} className="glass rounded-3xl border border-white/20 p-6 shadow-lg">
          <h3 className="mb-5 text-xl font-bold">Experience Timeline</h3>
          <Timeline />
        </motion.div>
      </div>
    </section>
  )
}
