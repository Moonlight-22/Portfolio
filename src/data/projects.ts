import Dashboard from '../assets/images/Dashboard_1.png'

export type Project = {
  id: string
  title: string
  description: string
  technologies: string[]
  image: string
  githubUrl: string
  liveUrl: string
}

export const projects: Project[] = [
  {
    id: 'eco-tech',
    title: 'Eco Tech',
    description: 'A platform for household food waste reduction, sustainability tracking, calorie management, and environmental impact analysis.',
    technologies: ['React', ' Python Flask', ' MySQL '],
    image: Dashboard,
    githubUrl: 'https://github.com/Moonlight-22/Eco-Tech.git',
    liveUrl: '',
  },
  
  {
    id: 'android-app',
    title: 'Android App (Offline Social)',
    description: 'Modern Android app focused on productivity, offline support, and performance.',
    technologies: ['Java', 'Android Studio', 'MySQL'],
    image: 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?q=80&w=1400&auto=format&fit=crop',
    githubUrl: '',
    liveUrl: 'https://example.com',
  },
  {
    id: 'portfolio-website',
    title: 'Portfolio Website',
    description: 'Animated personal portfolio with dark mode, responsive design, and smooth sections.',
    technologies: ['React', 'Tailwind', 'TypeScript'],
    image: 'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?q=80&w=1400&auto=format&fit=crop',
    githubUrl: 'https://github.com/',
    liveUrl: 'https://example.com',
  },
]
