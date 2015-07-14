#!/usr/bin/env bash

for i in {1..100}; do
  # Async
  echo "Async:";
  echo `time ./WithAsync.py > /dev/null 2>&1`;
  
  # Raw Executor
  echo "Raw:";
  echo `time ./WithRawExecutor.py > /dev/null 2>&1`;
  
  # Threads
  echo "Threads:";
  echo `time ./WithThreads.py > /dev/null 2>&1`
done
