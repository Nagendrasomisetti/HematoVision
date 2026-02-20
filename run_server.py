#!/usr/bin/env python
"""Flask application server runner with TensorFlow optimizations."""
import os
import sys
import signal

# Set TensorFlow optimization flags
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Ignore signals that might cause KeyboardInterrupt during import
def signal_handler(sig, frame):
    print(f"\nReceived signal {sig}, continuing...")
    pass

# Register signal handlers BEFORE importing TensorFlow
signal.signal(signal.SIGINT, signal_handler)
if hasattr(signal, 'SIGBREAK'):
    signal.signal(signal.SIGBREAK, signal_handler)

print("Loading TensorFlow...")
try:
    import tensorflow
    print(f"TensorFlow {tensorflow.__version__} loaded successfully")
except Exception as e:
    print(f"Error loading TensorFlow: {e}")
    sys.exit(1)

print("Loading Flask app...")
try:
    from app import app
    print("Flask app loaded successfully")
except Exception as e:
    print(f"Error loading Flask app: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("Starting Flask server...")
print("Server running on http://127.0.0.1:5000")
print("Press Ctrl+C to stop the server")
sys.stdout.flush()

try:
    app.run(debug=False, host="0.0.0.0", port=5000, use_reloader=False, threaded=True)
except KeyboardInterrupt:
    print("\nServer stopped by user")
    sys.exit(0)
except Exception as e:
    print(f"Server error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
