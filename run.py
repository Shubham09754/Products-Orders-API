import os
import uvicorn

if __name__ == "__main__":
    print("📦 Env variables:")
    for k, v in os.environ.items():
        if "PORT" in k:
            print(f"{k} = {v}")
    
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Starting on port {port}")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)

