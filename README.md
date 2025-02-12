git clone <repository-url>
cd <repository-name>
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Setup API Key

Ada 2 cara untuk mengatur Google API Key:

### Cara 1: Environment Variable
```bash
# Linux/Mac
export GOOGLE_API_KEY=your_api_key_here

# Windows (Command Prompt)
set GOOGLE_API_KEY=your_api_key_here

# Windows (PowerShell)
$env:GOOGLE_API_KEY="your_api_key_here"
```

### Cara 2: Config File
Buat file `config.json` di root folder:
```json
{
    "GOOGLE_API_KEY": "your_api_key_here"
}
```

4. Jalankan aplikasi
```bash
python main.py
```

Aplikasi akan berjalan di `http://localhost:5000`

## Fitur
- Chat dengan AI yang ramah dan gaul 😎
- Pembelajaran yang fun dan interaktif 🎮
- Penjelasan yang detail tapi tetap asik 📚
- Bisa beradaptasi dengan berbagai topik 🌈

## Deployment

### GitHub Pages
1. Fork repository ini
2. Setup GitHub Secrets untuk menyimpan API key:
   - Buka repository settings
   - Pilih "Secrets and variables" -> "Actions"
   - Klik "New repository secret"
   - Masukkan "GOOGLE_API_KEY" sebagai name
   - Paste API key kamu sebagai value
   - Klik "Add secret"
3. Enable GitHub Pages:
   - Buka repository settings
   - Pilih "Pages"
   - Pilih source (biasanya `main` branch)
   - Klik "Save"
4. Setup GitHub Actions:
   - Buat file `.github/workflows/deploy.yml`
   - Isi dengan konfigurasi untuk menggunakan secret:
   ```yaml
   name: Deploy to GitHub Pages
   on:
     push:
       branches: [ main ]
   jobs:
     deploy:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - name: Setup Python
           uses: actions/setup-python@v2
           with:
             python-version: '3.x'
         - name: Install Dependencies
           run: pip install -r requirements.txt
         - name: Build and Deploy
           env:
             GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
           run: |
             python main.py
   ```

### Hosting Lain
Pastikan untuk mengatur environment variable GOOGLE_API_KEY di platform hosting yang digunakan.

Contoh untuk beberapa platform:

#### Heroku
```bash
heroku config:set GOOGLE_API_KEY=your_api_key_here