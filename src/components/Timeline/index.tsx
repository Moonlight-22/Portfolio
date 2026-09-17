const experiences = [
  { year: '2026', title: 'Frontend Developer', description: 'Built responsive and accessible user interfaces for production apps.' },
  { year: '2025', title: 'Full Stack Intern', description: 'Worked on React and Spring Boot modules with reusable architecture.' },
  { year: '2024', title: 'CS Student Projects', description: 'Developed AI and web projects focused on practical outcomes.' },
]

export default function Timeline() {
  return (
    <ol className="relative space-y-6 border-l border-violet-300 pl-6 dark:border-violet-700">
      {experiences.map((item) => (
        <li key={item.year + item.title} className="relative">
          <span className="absolute -left-[1.8rem] top-1 h-3 w-3 rounded-full bg-violet-500" />
          <p className="text-sm font-semibold text-violet-500">{item.year}</p>
          <h3 className="mt-1 text-xl font-bold">{item.title}</h3>
          <p className="mt-1 text-slate-600 dark:text-slate-300">{item.description}</p>
        </li>
      ))}
    </ol>
  )
}
