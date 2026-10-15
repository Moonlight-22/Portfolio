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
    description: 'An AI-powered platform for reducing food waste with recipe suggestions, calorie tracking, and sustainability insights.',
    technologies: ['React', ' Python Flask', ' MySQL '],
    image: Dashboard,
    githubUrl: 'https://github.com/Moonlight-22/Eco-Tech.git',
    liveUrl: '',
  },
  {
    id: 'find-ace',
    title: 'Find Ace',
    description: 'A local marketplace for finding trusted workers, requesting and tracking jobs, and managing service reviews.',
    technologies: ['React 19', 'Vite', 'Tailwind CSS', 'Leaflet', 'Laravel 8', 'PHP 8', 'Laravel Sanctum', 'MySQL'],
    image: 'https://images.unsplash.com/photo-1581578731548-c64695cc6952?q=80&w=1400&auto=format&fit=crop',
    githubUrl: 'https://github.com/Moonlight-22/fullstack',
    liveUrl: '',
  },
  
  {
    id: 'android-app',
    title: 'Android App (Offline Social)',
    description: 'An offline-friendly Android social app built for productivity and performance.',
    technologies: ['Java', 'Android Studio', 'MySQL'],
    image: 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?q=80&w=1400&auto=format&fit=crop',
    githubUrl: '',
    liveUrl: 'https://example.com',
  },
  {
    id: 'portfolio-website',
    title: 'Portfolio Website',
    description: 'A responsive portfolio featuring dark mode, animation, and smooth navigation.',
    technologies: ['React', 'Tailwind', 'TypeScript'],
    image: 'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?q=80&w=1400&auto=format&fit=crop',
    githubUrl: 'https://github.com/',
    liveUrl: 'https://example.com',
  },
]
