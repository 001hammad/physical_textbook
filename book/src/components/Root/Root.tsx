import React, { useEffect } from 'react';
import { ChatbotProvider } from '@site/src/contexts/ChatbotContext';
import Chatbot from '@site/src/components/Chatbot/Chatbot';

const Root: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  useEffect(() => {
    // Add any global event listeners here if needed
    return () => {
      // Cleanup function if needed
    };
  }, []);

  return (
    <ChatbotProvider>
      {children}
    </ChatbotProvider>
  );
};

export default Root;