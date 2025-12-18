import type { ReactNode } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx(styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className={styles.heroTitle}>
          {siteConfig.title || 'Physical AI & Humanoid Robotics'}
        </Heading>
        <p className={styles.heroSubtitle}>
          {siteConfig.tagline || 'Build intelligent humanoid robots with ROS 2, Gazebo, Unity, and NVIDIA Isaac.'}
        </p>
        <div className={styles.buttons}>
          <Link
            className={`${styles.heroButton} ${styles.primaryButton}`}
            to="/docs/intro">
            Start Learning Now
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="Learn to build humanoid robots with Physical AI – ROS 2, simulation, and advanced perception."
    >
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}