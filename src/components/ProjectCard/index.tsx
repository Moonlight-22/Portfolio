import { motion } from 'framer-motion'
import { FaGithub } from 'react-icons/fa'
import { Link } from 'react-router-dom'
import type { Project } from '../../data/projects'

type Props = {
  project: Project
}

export default function ProjectCard({ project }: Props) {
  return (
    <motion.article
      whileHover={{ y: -6 }}
      className="overflow-hidden rounded-3xl border border-white/15 bg-white/70 shadow-lg transition dark:bg-[#11151b]"
    >
      <img src={project.image} alt={project.title} loading="lazy" className="h-48 w-full object-cover" />
      <div className="p-5">
        <h3 className="text-xl font-bold">{project.title}</h3>
        <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">{project.description}</p>
        <div className="mt-4 flex flex-wrap gap-2">
          {project.technologies.map((tech) => (
            <span key={tech} className="rounded-full bg-sky-100 px-3 py-1 text-xs font-semibold text-sky-800 dark:bg-sky-500/15 dark:text-sky-200">
              {tech}
            </span>
          ))}
        </div>
        <div className="mt-5 flex gap-3">
          <a href={project.githubUrl} target="_blank" rel="noreferrer" className="inline-flex items-center gap-2 rounded-full border border-slate-300 px-4 py-2 text-sm dark:border-slate-700">
            <FaGithub /> GitHub
          </a>
          <Link to={`/documents/${project.id}`} className="inline-flex items-center gap-2 rounded-full bg-sky-600 px-4 py-2 text-sm text-white transition hover:bg-sky-500">
            Document
          </Link>
        </div>
      </div>
    </motion.article>
  )
}
