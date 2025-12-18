import type { ReactNode } from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

// Feature items for your robotics book
const FeatureList = [
  {
    title: 'ROS 2 Mastery',
    description: (
      <>
        Learn the nervous system of modern robots. Control nodes, topics, services, and bridge AI agents to real hardware.
      </>
    ),
  },
  {
    title: 'Digital Twins Simulation',
    description: (
      <>
        Build safe, unlimited test environments with Gazebo & Unity. Simulate physics, sensors, and human interactions.
      </>
    ),
  },
  {
    title: 'AI-Powered Humanoids',
    description: (
      <>
        Integrate NVIDIA Isaac, GPT models, and Vision-Language-Action. Make robots see, think, talk, and act like humans.
      </>
    ),
  },
];

function Feature({ title, description }: { title: string; description: ReactNode }) {
  return (
    <div className={clsx('col col--4', styles.featureCard)}>
      <div className={styles.featureContent}>
        <Heading as="h3" className={styles.featureTitle}>
          {title}
        </Heading>
        <p className={styles.featureDesc}>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}