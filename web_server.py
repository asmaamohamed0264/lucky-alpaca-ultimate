#!/usr/bin/env python3
"""
🦙 Lucky Alpaca - Web Server
============================

FastAPI web server pentru Lucky Alpaca Ultimate Trading System
Oferă API endpoints pentru monitoring și control
"""

import asyncio
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from pathlib import Path

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel
import uvicorn

from loguru import logger
from dotenv import load_dotenv

<<<<<<< HEAD
<<<<<<< HEAD
# Import sistemele componente
from src.ai.ai_service_integration import ai_manager
=======
# Import sistemele componente (commented out for now to avoid import errors)
# from ultimate_trading_system import UltimateTradingSystem, UltimateTradingResults
# from src.api_clients.advanced_data_providers import AdvancedDataAggregator
# from src.ai.social_sentiment_analyzer import SocialSentimentAnalyzer
>>>>>>> 26696ddf1650dd9ba11897d402018e57d154aba6
=======
# Import sistemele componente
from ultimate_trading_system import UltimateTradingSystem, UltimateTradingResults
from src.api_clients.advanced_data_providers import AdvancedDataAggregator
from src.ai.social_sentiment_analyzer import SocialMediaSentimentAnalyzer
from src.ai.ai_service_integration import ai_manager
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203

load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Lucky Alpaca Ultimate Trading System",
    description="Advanced AI-powered trading system with social sentiment analysis",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure based on your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
# Global trading system instance (disabled for now)
# trading_system: Optional[UltimateTradingSystem] = None
# last_results: Optional[UltimateTradingResults] = None
=======
# Global trading system instance
trading_system: Optional[UltimateTradingSystem] = None
last_results: Optional[UltimateTradingResults] = None
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203

# Pydantic models
class HealthResponse(BaseModel):
    status: str
    timestamp: str
    uptime: str
    version: str
    system_health: Dict[str, Any]

class TradingStatusResponse(BaseModel):
    is_running: bool
    last_update: str
    total_signals: int
    active_positions: int
    portfolio_value: float
    daily_pnl: float

class SignalResponse(BaseModel):
    symbol: str
    signal_type: str
    strength: float
    confidence: float
    timestamp: str
    source: str

@app.on_event("startup")
async def startup_event():
    """Initialize the trading system on startup."""
<<<<<<< HEAD
    # global trading_system
=======
    global trading_system
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
    
    logger.info("🚀 Starting Lucky Alpaca Ultimate Trading System...")
    
    try:
<<<<<<< HEAD
        # Initialize trading system (disabled for now)
        # trading_system = UltimateTradingSystem()
        logger.success("✅ Lucky Alpaca Web Server initialized successfully")
        
        # Start background trading loop (disabled for now)
        # asyncio.create_task(background_trading_loop())
=======
        # Initialize trading system
        trading_system = UltimateTradingSystem()
        await trading_system.initialize()
        logger.success("✅ Lucky Alpaca Trading System initialized successfully")
        
        # Start background trading loop
        asyncio.create_task(background_trading_loop())
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize trading system: {e}")
        # Don't raise to allow server to start

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    logger.info("🛑 Shutting down Lucky Alpaca Trading System...")
    
<<<<<<< HEAD
    # if trading_system:
    #     await trading_system.shutdown()

# async def background_trading_loop():
#     """Background trading loop."""
#     global last_results
#     
#     while True:
#         try:
#             if trading_system:
#                 logger.info("🔄 Running trading cycle...")
#                 results = await trading_system.run_trading_cycle()
#                 last_results = results
#                 logger.success(f"✅ Trading cycle completed: {len(results.all_signals)} signals generated")
#             
#             # Wait 5 minutes between cycles
#             await asyncio.sleep(300)
#             
#         except Exception as e:
#             logger.error(f"❌ Error in trading loop: {e}")
#             await asyncio.sleep(60)  # Wait 1 minute on error
=======
    if trading_system:
        await trading_system.shutdown()

async def background_trading_loop():
    """Background trading loop."""
    global last_results
    
    while True:
        try:
            if trading_system:
                logger.info("🔄 Running trading cycle...")
                results = await trading_system.run_trading_cycle()
                last_results = results
                logger.success(f"✅ Trading cycle completed: {len(results.all_signals)} signals generated")
            
            # Wait 5 minutes between cycles
            await asyncio.sleep(300)
            
        except Exception as e:
            logger.error(f"❌ Error in trading loop: {e}")
            await asyncio.sleep(60)  # Wait 1 minute on error
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203

@app.get("/", response_class=HTMLResponse)
async def root():
    """Root endpoint with system information."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Lucky Alpaca Ultimate Trading System</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; text-align: center; }
            .status { background: #e8f5e8; padding: 15px; border-radius: 5px; margin: 20px 0; }
            .endpoints { background: #f8f9fa; padding: 15px; border-radius: 5px; }
            .endpoint { margin: 10px 0; padding: 10px; background: white; border-left: 4px solid #3498db; }
            a { color: #3498db; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🦙 Lucky Alpaca Ultimate Trading System</h1>
            <div class="status">
                <h3>✅ System Status: Running</h3>
                <p>Advanced AI-powered trading system with social sentiment analysis</p>
            </div>
            <div class="endpoints">
                <h3>📡 Available Endpoints:</h3>
                <div class="endpoint">
                    <strong>GET /health</strong> - System health check
                </div>
                <div class="endpoint">
                    <strong>GET /status</strong> - Trading system status
                </div>
                <div class="endpoint">
                    <strong>GET /signals</strong> - Latest trading signals
                </div>
                <div class="endpoint">
                    <strong>GET /portfolio</strong> - Portfolio information
                </div>
                <div class="endpoint">
                    <strong>GET /docs</strong> - API documentation
                </div>
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
                <div class="endpoint">
                    <strong>GET /ai/services</strong> - Available AI services
                </div>
                <div class="endpoint">
                    <strong>POST /ai/sentiment</strong> - Analyze sentiment with AI
                </div>
                <div class="endpoint">
<<<<<<< HEAD
                    <strong>POST /ai/sentiment/local</strong> - Analyze sentiment with FinBERT
                </div>
                <div class="endpoint">
                    <strong>POST /ai/signal</strong> - Generate trading signal with AI
                </div>
=======
>>>>>>> 26696ddf1650dd9ba11897d402018e57d154aba6
=======
                    <strong>POST /ai/signal</strong> - Generate trading signal with AI
                </div>
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    try:
        # Check system health
        system_health = {
            "trading_system": trading_system is not None,
            "last_results": last_results is not None,
            "environment": os.getenv("ENVIRONMENT", "development"),
            "port": os.getenv("PORT", "8000")
        }
        
        return HealthResponse(
            status="healthy",
            timestamp=datetime.now().isoformat(),
            uptime="running",
            version="1.0.0",
            system_health=system_health
        )
        
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=500, detail="Health check failed")

@app.get("/status", response_model=TradingStatusResponse)
async def get_trading_status():
    """Get trading system status."""
    try:
<<<<<<< HEAD
        # Return basic status without trading system
        return TradingStatusResponse(
            is_running=True,
            last_update=datetime.now().isoformat(),
            total_signals=0,
            active_positions=0,
            portfolio_value=0.0,
            daily_pnl=0.0
=======
        if not trading_system:
            raise HTTPException(status_code=503, detail="Trading system not initialized")
        
        return TradingStatusResponse(
            is_running=trading_system.is_running,
            last_update=datetime.now().isoformat(),
            total_signals=len(last_results.all_signals) if last_results else 0,
            active_positions=len(await trading_system.alpaca_client.get_positions()),
            portfolio_value=(await trading_system.alpaca_client.get_account()).portfolio_value,
            daily_pnl=(await trading_system.alpaca_client.get_account()).equity - (await trading_system.alpaca_client.get_account()).last_equity
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
        )
        
    except Exception as e:
        logger.error(f"Error getting trading status: {e}")
        raise HTTPException(status_code=500, detail="Failed to get trading status")

@app.get("/signals", response_model=List[SignalResponse])
async def get_latest_signals():
    """Get latest trading signals."""
    try:
<<<<<<< HEAD
        # Return empty signals for now
=======
        if not trading_system:
            raise HTTPException(status_code=503, detail="Trading system not initialized")
        
        if last_results:
            return [
                SignalResponse(
                    symbol=s.symbol,
                    signal_type=s.signal_type,
                    strength=s.strength,
                    confidence=s.confidence,
                    timestamp=s.timestamp.isoformat(),
                    source=s.source
                ) for s in last_results.all_signals
            ]
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
        return []
        
    except Exception as e:
        logger.error(f"Error getting signals: {e}")
        raise HTTPException(status_code=500, detail="Failed to get signals")

@app.get("/portfolio")
async def get_portfolio():
    """Get portfolio information."""
    try:
<<<<<<< HEAD
        # Return basic portfolio info
        return {
            "timestamp": datetime.now().isoformat(),
            "portfolio_value": 0.0,
            "daily_pnl": 0.0,
            "total_signals": 0,
            "recommendations": []
=======
        if not trading_system:
            raise HTTPException(status_code=503, detail="Trading system not initialized")
        
        account = await trading_system.alpaca_client.get_account()
        positions = await trading_system.alpaca_client.get_positions()
        
        return {
            "timestamp": datetime.now().isoformat(),
            "portfolio_value": account.portfolio_value,
            "daily_pnl": account.equity - account.last_equity,
            "total_signals": len(last_results.all_signals) if last_results else 0,
            "positions": [p.dict() for p in positions],
            "recommendations": last_results.portfolio_recommendations if last_results else []
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
        }
        
    except Exception as e:
        logger.error(f"Error getting portfolio: {e}")
        raise HTTPException(status_code=500, detail="Failed to get portfolio")

@app.post("/start")
async def start_trading():
    """Start trading system."""
    try:
<<<<<<< HEAD
        logger.info("🚀 Trading system start requested...")
        return {"message": "Trading system ready to start", "status": "success"}
=======
        global trading_system
        if not trading_system:
            trading_system = UltimateTradingSystem()
            await trading_system.initialize()
        asyncio.create_task(background_trading_loop())
        return {"message": "Trading system started", "status": "running"}
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
            
    except Exception as e:
        logger.error(f"Error starting trading: {e}")
        raise HTTPException(status_code=500, detail="Failed to start trading")

@app.post("/stop")
async def stop_trading():
    """Stop trading system."""
    try:
<<<<<<< HEAD
        logger.info("🛑 Trading system stop requested...")
        return {"message": "Trading system stopped", "status": "success"}
=======
        global trading_system
        if trading_system:
            await trading_system.shutdown()
            trading_system = None
        return {"message": "Trading system stopped", "status": "stopped"}
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
            
    except Exception as e:
        logger.error(f"Error stopping trading: {e}")
        raise HTTPException(status_code=500, detail="Failed to stop trading")

<<<<<<< HEAD
<<<<<<< HEAD
# AI Service Endpoints
=======
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
@app.get("/ai/services")
async def get_ai_services():
    """Get available AI services."""
    try:
        services = ai_manager.get_available_services()
        return {
            "services": services,
            "total_available": len([s for s in services if s["available"]]),
            "total_services": len(services)
        }
    except Exception as e:
        logger.error(f"Error getting AI services: {e}")
        raise HTTPException(status_code=500, detail="Failed to get AI services")

@app.post("/ai/test/{service_name}")
async def test_ai_service(service_name: str):
    """Test an AI service."""
    try:
        result = await ai_manager.test_service(service_name)
        return result
    except Exception as e:
        logger.error(f"Error testing AI service {service_name}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to test AI service: {e}")

@app.post("/ai/sentiment")
async def analyze_sentiment(text: str, service: str = "nvidia_nim"):
    """Analyze sentiment using AI service."""
    try:
        result = await ai_manager.analyze_sentiment(text, service)
        return {
            "text": text,
            "service": service,
            "analysis": result,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Error analyzing sentiment: {e}")
        raise HTTPException(status_code=500, detail="Failed to analyze sentiment")

<<<<<<< HEAD
@app.post("/ai/sentiment/local")
async def analyze_sentiment_local(text: str):
    """Analyze sentiment using local FinBERT."""
    try:
        result = await ai_manager.analyze_sentiment_local(text)
        return {
            "text": text,
            "service": "finbert_local",
            "analysis": result,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Error analyzing sentiment locally: {e}")
        raise HTTPException(status_code=500, detail="Failed to analyze sentiment locally")

=======
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
@app.post("/ai/signal")
async def generate_trading_signal(market_data: Dict[str, Any], service: str = "gemini"):
    """Generate trading signal using AI service."""
    try:
        result = await ai_manager.generate_trading_signal(market_data, service)
        return {
            "market_data": market_data,
            "service": service,
            "signal": result,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Error generating trading signal: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate trading signal")

<<<<<<< HEAD
=======
>>>>>>> 26696ddf1650dd9ba11897d402018e57d154aba6
=======
>>>>>>> c9ac10bed887a2439883d5d5dafad0c3af378203
if __name__ == "__main__":
    # Get configuration from environment
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    
    logger.info(f"🚀 Starting Lucky Alpaca Web Server on {host}:{port}")
    
    # Run the server
    uvicorn.run(
        "web_server:app",
        host=host,
        port=port,
        reload=False,
        log_level="info"
    )
