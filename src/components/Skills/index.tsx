import { motion } from 'framer-motion'
import { FaCode, FaImage, FaJava, FaPalette, FaPen, FaRobot, FaSitemap, FaTools } from 'react-icons/fa'
import type { IconType } from 'react-icons'
import {
  SiAndroidstudio,
  SiBootstrap,
  SiCss,
  SiCursor,
  SiDavinciresolve,
  SiDocker,
  SiFigma,
  SiFlask,
  SiGit,
  SiGithub,
  SiGooglegemini,
  SiHtml5,
  SiJavascript,
  SiLaravel,
  SiMysql,
  SiOpencv,
  SiPhp,
  SiPostgresql,
  SiPostman,
  SiPython,
  SiQwen,
  SiReact,
  SiScikitlearn,
  SiSpringboot,
  SiSupabase,
  SiTailwindcss,
  SiTensorflow,
} from 'react-icons/si'
import { skills } from '../../data/skills'
import SectionTitle from '../SectionTitle'

const skillIcons: Record<string, IconType> = {
  React: SiReact,
  JavaScript: SiJavascript,
  HTML: SiHtml5,
  CSS: SiCss,
  Tailwind: SiTailwindcss,
  Bootstrap: SiBootstrap,
  Java: FaJava,
  'Spring Boot': SiSpringboot,
  Python: SiPython,
  Flask: SiFlask,
  PHP: SiPhp,
  Laravel: SiLaravel,
  MySQL: SiMysql,
  PostgreSQL: SiPostgresql,
  Supabase: SiSupabase,
  'Android Studio': SiAndroidstudio,
  Docker: SiDocker,
  Figma: SiFigma,
  Git: SiGit,
  GitHub: SiGithub,
  Postman: SiPostman,
  TensorFlow: SiTensorflow,
  OpenCV: SiOpencv,
  'Scikit-learn': SiScikitlearn,
  Gemini: SiGooglegemini,
  Qwen: SiQwen,
  Cursor: SiCursor,
  'DaVinci Resolve': SiDavinciresolve,
  Canva: FaPalette,
  'Adobe Photoshop': FaImage,
  'Adobe Illustrator': FaPen,
  StarUML: FaSitemap,
  'VS Code': FaCode,
  ChatGPT: FaRobot,
}

export default function Skills() {
  return (
    <section id="skills" className="mx-auto max-w-6xl px-4 py-16 md:px-6">
      <SectionTitle eyebrow="Skills" title="Technical Skills" />
      <div className="grid gap-5 md:grid-cols-2">
        {skills.map((group) => (
          <motion.article key={group.category} whileInView={{ opacity: 1, y: 0 }} initial={{ opacity: 0, y: 18 }} viewport={{ once: true }} className="glass rounded-3xl border border-white/20 p-5 shadow-lg">
            <h3 className="mb-4 text-xl font-bold">{group.category}</h3>
            <div className="space-y-3">
              {group.items.map((skill) => (
                <div key={skill.name} className="rounded-2xl border border-white/5 bg-white/[0.03] p-3">
                  <div className="mb-2 flex items-center gap-3">
                    <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-sky-500/10 text-lg text-sky-300">
                      {(() => {
                        const Icon = skillIcons[skill.name] ?? FaTools
                        return <Icon aria-hidden="true" />
                      })()}
                    </span>
                    <div className="min-w-0 flex-1">
                      <div className="flex items-center justify-between gap-2 text-sm">
                        <span className="truncate font-medium">{skill.name}</span>
                        <span className="shrink-0 text-xs font-semibold text-sky-300">{skill.level}%</span>
                      </div>
                      <div
                        className="mt-2 h-1.5 overflow-hidden rounded-full bg-slate-200 dark:bg-slate-800"
                        role="meter"
                        aria-label={`${skill.name} rating`}
                        aria-valuemin={0}
                        aria-valuemax={100}
                        aria-valuenow={skill.level}
                      >
                        <motion.div
                          initial={{ width: 0 }}
                          whileInView={{ width: `${skill.level}%` }}
                          viewport={{ once: true }}
                          transition={{ duration: 0.8 }}
                          className="h-full rounded-full bg-gradient-to-r from-blue-500 to-sky-300"
                        />
                      </div>
                    </div>
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
