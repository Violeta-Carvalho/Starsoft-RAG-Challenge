#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

# Pull model if it wasn't pulled before
MODELS=$(ollama list)
if [[ $MODELS != *"llama3.1"* ]]; then
    echo "🔴 Retrieve LLAMA3.1 model..."
    ollama pull llama3.1
    echo "🟢 Done!"
fi

# Wait for Ollama process to finish.
wait $pid