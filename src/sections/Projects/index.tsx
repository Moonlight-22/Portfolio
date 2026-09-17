import { useMemo, useState } from 'react'
import { projects } from '../../data/projects'
import ProjectCard from '../../components/ProjectCard'
import SectionTitle from '../../components/SectionTitle'

export default function ProjectsSection() {
  const [filter, setFilter] = useState('All')
  const technologies = useMemo(() => ['All', ...new Set(projects.flatMap((project) => project.technologies))], [])
  const filtered = useMemo(
    () => (filter === 'All' ? projects : projects.filter((project) => project.technologies.includes(filter))),
    [filter],
  )

  return (
    <section id="projects" className="mx-auto max-w-6xl px-4 py-16 md:px-6">
      <SectionTitle eyebrow="Projects" title="Featured Projects" subtitle="Reusable project cards with hover interaction and tech filtering." />
      <div className="mb-6 flex flex-wrap gap-2">
        {technologies.map((item) => (
          <button
            key={item}
            type="button"
            onClick={() => setFilter(item)}
            className={`rounded-full px-4 py-2 text-sm ${
              filter === item
                ? 'bg-violet-600 text-white'
                : 'border border-slate-300 text-slate-700 dark:border-slate-700 dark:text-slate-200'
            }`}
          >
            {item}
          </button>
        ))}
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        {filtered.map((project) => (
          <ProjectCard key={project.id} project={project} />
        ))}
      </div>
    </section>
  )
}
