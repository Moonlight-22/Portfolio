import { motion } from 'framer-motion'
import { skills } from '../../data/skills'
import SectionTitle from '../SectionTitle'

export default function Skills() {
  return (
    <section id="skills" className="mx-auto max-w-6xl px-4 py-16 md:px-6">
      <SectionTitle eyebrow="Skills" title="Technical Skills" subtitle="Grouped by category with animated progress indicators." />
      <div className="grid gap-5 md:grid-cols-2">
        {skills.map((group) => (
          <motion.article key={group.category} whileInView={{ opacity: 1, y: 0 }} initial={{ opacity: 0, y: 18 }} viewport={{ once: true }} className="glass rounded-3xl border border-white/20 p-5 shadow-lg">
            <h3 className="mb-4 text-xl font-bold">{group.category}</h3>
            <div className="space-y-3">
              {group.items.map((skill) => (
                <div key={skill.name}>
                  <div className="mb-1 flex justify-between text-sm">
                    <span>{skill.name}</span>
                    <span>{skill.level}%</span>
                  </div>
                  <div className="h-2 rounded-full bg-slate-200 dark:bg-slate-800">
                    <motion.div
                      initial={{ width: 0 }}
                      whileInView={{ width: `${skill.level}%` }}
                      viewport={{ once: true }}
                      transition={{ duration: 0.8 }}
                      className="h-2 rounded-full bg-gradient-to-r from-violet-500 to-cyan-500"
                    />
                  </div>
                </div>
              ))}
            </div>
          </motion.article>
        ))}
      </div>
    </section>
  )
}
