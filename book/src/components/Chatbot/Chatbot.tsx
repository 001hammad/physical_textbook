import React, { useState, useEffect, useRef } from 'react';
import clsx from 'clsx';
import styles from './Chatbot.module.css';

interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: Date;
}

interface ChatResponse {
  response_id: string;
  answer: string;
  sources: string[];
  confidence: number;
  message?: string;
}

const Chatbot: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState<string>('');
  const [mode, setMode] = useState<'normal' | 'selected-text'>('normal');
  const [isExpanded, setIsExpanded] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    // Add user message to chat
    const userMessage: Message = {
      id: Date.now().toString(),
      content: inputValue,
      role: 'user',
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Prepare the request body based on the current mode
      const requestBody = {
        question: inputValue,
        mode: mode,
        ...(mode === 'selected-text' && selectedText && { selected_text: selectedText }),
      };

      // Call the backend API
      const response = await fetch('https://hammad224-chatbot-backend.hf.space/api/v1/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: ChatResponse = await response.json();

      // Add assistant response to chat
      const assistantMessage: Message = {
        id: Date.now().toString(),
        content: data.answer,
        role: 'assistant',
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error sending message:', error);

      // Add error message to chat
      const errorMessage: Message = {
        id: Date.now().toString(),
        content: 'Sorry, I encountered an error. Please try again.',
        role: 'assistant',
        timestamp: new Date(),
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleModeToggle = (newMode: 'normal' | 'selected-text') => {
    setMode(newMode);
    if (newMode === 'normal') {
      setSelectedText('');
    }
  };

  // Function to handle text selection from the page
  const handleTextSelection = () => {
    const selectedText = window.getSelection()?.toString().trim() || '';
    if (selectedText) {
      setSelectedText(selectedText);
      setMode('selected-text');
    }
  };

  // Effect to add event listener for text selection
  useEffect(() => {
    const handleGlobalSelection = () => {
      setTimeout(() => {
        const selectedText = window.getSelection()?.toString().trim() || '';
        if (selectedText.length > 0) {
          setSelectedText(selectedText);
          setMode('selected-text');
        }
      }, 0);
    };

    document.addEventListener('mouseup', handleGlobalSelection);
    return () => {
      document.removeEventListener('mouseup', handleGlobalSelection);
    };
  }, []);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <div className={clsx(styles.chatbotContainer, isExpanded ? styles.expanded : styles.collapsed)}>
      <div className={styles.chatbotHeader} onClick={toggleExpand}>
        <h3 className={styles.chatbotTitle}>AI</h3>
        <span className={styles.expandIcon}>{isExpanded ? '−' : '+'}</span>
      </div>

      {isExpanded && (
        <div className={styles.chatbotContent}>
          {/* Mode Selection */}
          <div className={styles.modeSelector}>
            <button
              className={clsx(styles.modeButton, mode === 'normal' && styles.activeMode)}
              onClick={() => handleModeToggle('normal')}
            >
              Normal Question
            </button>
            <button
              className={clsx(styles.modeButton, mode === 'selected-text' && styles.activeMode)}
              onClick={() => handleModeToggle('selected-text')}
            >
              Selected Text
            </button>
          </div>

          {/* Selected Text Display */}
          {mode === 'selected-text' && selectedText && (
            <div className={styles.selectedTextDisplay}>
              <p><strong>Selected text:</strong></p>
              <p className={styles.selectedText}>{selectedText.substring(0, 100)}{selectedText.length > 100 ? '...' : ''}</p>
            </div>
          )}

          {/* Chat Messages */}
          <div className={styles.chatMessages}>
            {messages.length === 0 ? (
              <div className={styles.welcomeMessage}>
                <p>Hello! I'm your AI assistant for the Physical AI & Humanoid Robotics book.</p>
                <p>You can ask me questions about the book content or analyze selected text.</p>
              </div>
            ) : (
              messages.map((message) => (
                <div
                  key={message.id}
                  className={clsx(
                    styles.message,
                    message.role === 'user' ? styles.userMessage : styles.assistantMessage
                  )}
                >
                  <div className={styles.messageContent}>{message.content}</div>
                  <div className={styles.messageTimestamp}>
                    {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </div>
                </div>
              ))
            )}
            {isLoading && (
              <div className={styles.message + ' ' + styles.assistantMessage}>
                <div className={styles.typingIndicator}>
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div className={styles.inputArea}>
            <textarea
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={
                mode === 'normal'
                  ? 'Ask a question about the book content...'
                  : selectedText
                    ? 'Ask about the selected text...'
                    : 'Select text on the page first, or ask a general question...'
              }
              className={styles.inputField}
              rows={3}
              disabled={isLoading}
            />
            <button
              onClick={handleSendMessage}
              disabled={!inputValue.trim() || isLoading}
              className={clsx(styles.sendButton, (!inputValue.trim() || isLoading) && styles.disabled)}
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Chatbot;