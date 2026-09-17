import { motion } from 'framer-motion'
import { FaExternalLinkAlt, FaGithub } from 'react-icons/fa'
import type { Project } from '../../data/projects'

type Props = {
  project: Project
}

export default function ProjectCard({ project }: Props) {
  return (
    <motion.article
      whileHover={{ y: -6 }}
      className="overflow-hidden rounded-3xl border border-white/20 bg-white/70 shadow-lg transition dark:bg-slate-900/70"
    >
      <img src={project.image} alt={project.title} loading="lazy" className="h-48 w-full object-cover" />
      <div className="p-5">
        <h3 className="text-xl font-bold">{project.title}</h3>
        <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">{project.description}</p>
        <div className="mt-4 flex flex-wrap gap-2">
          {project.technologies.map((tech) => (
            <span key={tech} className="rounded-full bg-violet-100 px-3 py-1 text-xs font-semibold text-violet-700 dark:bg-violet-500/20 dark:text-violet-200">
              {tech}
            </span>
          ))}
        </div>
        <div className="mt-5 flex gap-3">
          <a href={project.githubUrl} target="_blank" rel="noreferrer" className="inline-flex items-center gap-2 rounded-full border border-slate-300 px-4 py-2 text-sm dark:border-slate-700">
            <FaGithub /> GitHub
          </a>
          <a href={project.liveUrl} target="_blank" rel="noreferrer" className="inline-flex items-center gap-2 rounded-full bg-violet-600 px-4 py-2 text-sm text-white">
            <FaExternalLinkAlt /> Document                                                                                                                                                                                                               
          </a>
        </div>
      </div>
    </motion.article>
  )
}
