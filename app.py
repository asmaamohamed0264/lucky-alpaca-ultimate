<<<<<<< HEAD
#!/usr/bin/env python3
"""
🦙 Lucky Alpaca - Main Application Entry Point
=======
﻿#!/usr/bin/env python3
"""
ðŸ¦™ Lucky Alpaca - Main Application Entry Point
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
==============================================

Entry point pentru Lucky Alpaca Ultimate Trading System
"""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Import and run the web server
if __name__ == "__main__":
<<<<<<< HEAD
    print("🚀 Starting Lucky Alpaca Ultimate Trading System...")
    print("📊 Web server will be available at http://0.0.0.0:8000")
    print("🔧 Health check: http://0.0.0.0:8000/health")
=======
    print("ðŸš€ Starting Lucky Alpaca Ultimate Trading System...")
    print("ðŸ“Š Web server will be available at http://0.0.0.0:8000")
    print("ðŸ”§ Health check: http://0.0.0.0:8000/health")
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
    
    # Import and run web server
    from web_server import app
    import uvicorn
    
    # Get configuration from environment
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    
<<<<<<< HEAD
    print(f"🌐 Starting server on {host}:{port}")
=======
    print(f"ðŸŒ Starting server on {host}:{port}")
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
    
    # Run the server
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=False,
        log_level="info"
    )
