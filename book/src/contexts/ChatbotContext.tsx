import React, { createContext, useContext, useState, ReactNode } from 'react';

interface ChatbotContextType {
  isChatbotVisible: boolean;
  toggleChatbotVisibility: () => void;
  selectedText: string | null;
  setSelectedText: (text: string | null) => void;
}

const ChatbotContext = createContext<ChatbotContextType | undefined>(undefined);

export const ChatbotProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [isChatbotVisible, setIsChatbotVisible] = useState(true); // Ensure it's visible by default
  const [selectedText, setSelectedText] = useState<string | null>(null);

  const toggleChatbotVisibility = () => {
    setIsChatbotVisible(prev => !prev);
  };

  return (
    <ChatbotContext.Provider value={{
      isChatbotVisible,
      toggleChatbotVisibility,
      selectedText,
      setSelectedText
    }}>
      {children}
    </ChatbotContext.Provider>
  );
};

export const useChatbot = () => {
  const context = useContext(ChatbotContext);
  if (context === undefined) {
    throw new Error('useChatbot must be used within a ChatbotProvider');
  }
  return context;
};