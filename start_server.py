#!/usr/bin/env python
"""Robust Flask server runner with signal handling."""
import os
import sys
import signal

# Suppress keyboard interrupt during startup
original_sigint = signal.signal(signal.SIGINT, signal.SIG_IGN)

try:
    # Change to app directory
    app_dir = r'e:\Nagendra\projects\HematoVision-Advanced-Blood-Cell-Classification-Using-Transfer-Learning-by-LTVIP2025TMID44712-main\HematoVision-Advanced-Blood-Cell-Classification-Using-Transfer-Learning'
    os.chdir(app_dir)
    sys.path.insert(0, app_dir)

    # Set environment variables
    os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    print("=" * 70)
    print("HematoVision Blood Cell Classification Server")
    print("=" * 70)
    print(f"Working directory: {os.getcwd()}")
    print(f"Python executable: {sys.executable}")

    print("\n[1/3] Loading TensorFlow (this may take 1-2 minutes)...")
    sys.stdout.flush()
    
    import tensorflow as tf
    print(f"      ✓ TensorFlow {tf.__version__} loaded successfully")
    sys.stdout.flush()

    print("\n[2/3] Loading Flask application...")
    sys.stdout.flush()
    
    from app import app
    print("      ✓ Flask app loaded successfully")
    sys.stdout.flush()

    # Restore signal handling
    signal.signal(signal.SIGINT, original_sigint)

    print("\n[3/3] Starting Flask server...")
    print("-" * 70)
    print("Server URLs:")
    print("  • Local:   http://127.0.0.1:5000")
    print("  • Network: http://192.168.55.104:5000")
    print("-" * 70)
    print("Press Ctrl+C to stop the server\n")
    sys.stdout.flush()

    # Run the Flask app
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True,
        use_debugger=False
    )

except KeyboardInterrupt:
    print("\n\nServer stopped by user")
    sys.exit(0)
except Exception as e:
    print(f"\n\nError during startup: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
finally:
    # Restore original signal handler
    signal.signal(signal.SIGINT, original_sigint)
