import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

function ChatbotTestPage() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout title={`Chatbot Test - ${siteConfig.title}`} description="Test page for the RAG Chatbot integration">
      <div className="container" style={{ padding: '2rem', maxWidth: '1200px', margin: '0 auto' }}>
        <div className="row">
          <div className="col col--8 col--offset-2">
            <h1>Chatbot Integration Test</h1>
            <p>
              This page demonstrates the RAG Chatbot integration with the Physical AI & Humanoid Robotics book.
            </p>

            <h2>How to Use</h2>
            <ol>
              <li><strong>Normal Mode</strong>: Type your question in the chatbot and get answers from the book content</li>
              <li><strong>Selected Text Mode</strong>: Select text on this page, then switch to "Selected Text" mode in the chatbot</li>
            </ol>

            <h2>Try It Out</h2>
            <p>
              Select some text on this page (like this paragraph) and the chatbot will automatically switch to "Selected Text" mode.
              You can then ask questions specifically about the selected text.
            </p>

            <p>
              This is a sample paragraph for testing text selection. Try selecting this text and then asking the chatbot about it.
              The chatbot will focus its response on the selected text rather than searching the entire book.
            </p>

            <p>
              The chatbot is built with a RAG (Retrieval Augmented Generation) architecture that ensures responses are based only
              on the book content, preventing hallucinations. It uses Cohere for embeddings, Qdrant for vector storage, and Gemini
              for response generation.
            </p>

            <div style={{ marginTop: '2rem', padding: '1rem', backgroundColor: '#f0f8ff', border: '1px solid #33fcff', borderRadius: '8px' }}>
              <h3>Troubleshooting</h3>
              <p>
                If the chatbot doesn't work, make sure the backend server is running:
              </p>
              <pre style={{ backgroundColor: '#000', color: '#33fcff', padding: '0.5rem', borderRadius: '4px' }}>
                cd chatbot/backend<br/>
                uvicorn src.api.main:app --reload --port 8000
              </pre>
            </div>

            <div style={{ marginTop: '1rem' }}>
              <Link to="/" className="button button--primary">
                Back to Home
              </Link>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default ChatbotTestPage;