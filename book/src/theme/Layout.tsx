import React from 'react';
import OriginalLayout from '@theme-original/Layout';
import { ChatbotProvider } from '@site/src/contexts/ChatbotContext';
import Chatbot from '@site/src/components/Chatbot/Chatbot';

export default function Layout(props) {
  return (
    <ChatbotProvider>
      <OriginalLayout {...props}>
        {props.children}
        <Chatbot />
      </OriginalLayout>
    </ChatbotProvider>
  );
}