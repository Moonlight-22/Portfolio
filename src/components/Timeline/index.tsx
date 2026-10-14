const experiences = [
  { year: '2025', title: 'Freelance Developer and Computer Tutor', description: 'Built responsive and accessible UI for production apps and Conducted courses on basic to advanced, and system maintenance best practices.' },
  { year: '2024', title: 'Freelance Graphic Designer', description: 'Delivered detailed visual content and marketing collaterals using Figma, Canva, and Adobe tools. ' },
  { year: '2023', title: 'IT Support Specialist', description: 'Provided first-line technical support, system maintenance, and network troubleshooting for office workstations. ' },
]

export default function Timeline() {
  return (
    <ol className="relative space-y-6 border-l border-sky-300/50 pl-6 dark:border-sky-700">
      {experiences.map((item) => (
        <li key={item.year + item.title} className="relative">
          <span className="absolute -left-[1.8rem] top-1 h-3 w-3 rounded-full bg-sky-500" />
          <p className="text-sm font-semibold text-sky-400">{item.year}</p>
          <h3 className="mt-1 text-xl font-bold">{item.title}</h3>
          <p className="mt-1 text-slate-600 dark:text-slate-300">{item.description}</p>
        </li>
      ))}
    </ol>
  )
}
