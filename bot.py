import os
import datetime
import google.generativeai as genai

api_key = os.environ.get("OPENAI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_content():
    prompt = "Cara pembuatan WEB yang menarik dan simple."
    response = model.generate_content(prompt)
    return response.text

def main():
    content = generate_content()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"\n\n--- Update: {timestamp} ---\n{content}\n"
    
    # Simpan ke file log atau file kode
    with open("activity_log.md", "a", encoding="utf-8") as f:
        f.write(log_entry)
        
    print("Konten AI berhasil digenerate dan ditulis ke file.")

if __name__ == "__main__":
    main()
