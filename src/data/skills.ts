export type SkillCategory = {
  category: string
  items: { name: string; level: number }[]
}

export const skills: SkillCategory[] = [
  {
    category: 'Frontend',
    items: [
      { name: 'React', level: 90 },
      { name: 'JavaScript', level: 90 },
      { name: 'HTML', level: 95 },
      { name: 'CSS', level: 90 },
      { name: 'Tailwind', level: 88 },
    ],
  },
  {
    category: 'Backend',
    items: [
      { name: 'Java', level: 80 },
      { name: 'Spring Boot', level: 78 },
      { name: 'Python', level: 85 },
      { name: 'Flask', level: 75 },
      { name: 'PHP', level: 70 },
    ],
  },
  {
    category: 'Database',
    items: [{ name: 'MySQL', level: 82 }],
  },
  {
    category: 'Machine Learning',
    items: [
      { name: 'TensorFlow', level: 78 },
      { name: 'OpenCV', level: 75 },
      { name: 'Scikit-learn', level: 80 },
    ],
  },
  {
    category: 'Tools',
    items: [
      { name: 'Git', level: 88 },
      { name: 'GitHub', level: 90 },
      { name: 'Android Studio', level: 75 },
      { name: 'VS Code', level: 93 },
      { name: 'Figma', level: 70 },
    ],
  },
]
