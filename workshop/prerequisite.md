# 📋 Prerequisites

Welcome to the GitHub Copilot Workshop! This guide will help you set up the necessary tools and authentication to get started with GitHub Copilot.

## 🚀 Quick Start Checklist

- [ ] Install Node.js and npm
- [ ] Install GitHub Copilot CLI
- [ ] Authenticate with GitHub
- [ ] Install GitHub Copilot in VS Code
- [ ] Verify your setup

---

## 📦 Installing Node.js and npm

Before installing the GitHub Copilot CLI, you need to have Node.js and npm installed on your system.

### Windows

**Option 1: Using the Installer**
1. Visit [nodejs.org](https://nodejs.org/)
2. Download the LTS (Long Term Support) version
3. Run the installer and follow the installation wizard
4. Verify installation by opening PowerShell and running:
   ```powershell
   node --version
   npm --version
   ```

**Option 2: Using Winget**
```powershell
winget install OpenJS.NodeJS.LTS
```

### macOS

**Option 1: Using Homebrew**
```bash
brew install node
```

**Option 2: Using the Installer**
1. Visit [nodejs.org](https://nodejs.org/)
2. Download the LTS version for macOS
3. Run the installer

Verify installation:
```bash
node --version
npm --version
```

### Linux

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install nodejs npm
```

**Fedora:**
```bash
sudo dnf install nodejs npm
```

**Using Node Version Manager (nvm) - Recommended for all Linux distributions:**
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install --lts
```

Verify installation:
```bash
node --version
npm --version
```

---

## 🔧 Installing GitHub Copilot CLI

### Installation

Install the Copilot CLI globally using npm:

```bash
npm install -g @github/copilot
```

### Launching the CLI

Once installed, launch the CLI with:

```bash
copilot
```

> 💡 **Tip:** Launch `copilot` in a folder that contains code you want to work with for the best experience.

---

## 🔐 Authentication

### Method 1: Interactive Login

If you're not currently logged in to GitHub, you'll be prompted to use the `/login` slash command. Enter this command and follow the on-screen instructions to authenticate.

### Method 2: Personal Access Token (PAT)

For automated workflows or when interactive login isn't suitable, you can authenticate using a fine-grained PAT:

1. **Create a new token:** Visit [GitHub Personal Access Tokens](https://github.com/settings/personal-access-tokens/new)
2. **Set permissions:** Under "Permissions," click "add permissions" and select **"Copilot Requests"**
3. **Generate your token:** Complete the token creation process
4. **Set environment variable:** Add the token to your environment using either:
   - `GH_TOKEN` (higher precedence)
   - `GITHUB_TOKEN`

### Using the CLI

🎯 **Model Selection:** By default, `copilot` utilizes **Claude Sonnet 4.5**. Use the `/model` slash command to choose from other available models, including:
- Claude Sonnet 4
- GPT-5

---

## 🎨 Installing GitHub Copilot in Visual Studio Code

### Step-by-Step Installation

1. **Open VS Code**

2. **Access Extensions:** Go to the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X` on Mac)

3. **Install Copilot:** Search for **"GitHub Copilot"** and click **"Install"**

4. **Authenticate:** Sign in to your GitHub account when prompted and authorize the extension

5. **Activate:** After installation, reload VS Code to enable Copilot

### Setting Up Your Subscription

> ℹ️ **Note:** You need access to a GitHub Copilot subscription to use the service.

**Quick Setup from VS Code:**
1. Hover over the **Copilot icon** in the Status Bar
2. Select **"Set up Copilot"**
3. Choose a sign-in method and follow the prompts
4. If you don't have a subscription, you'll be signed up for the **Copilot Free plan**

---

## ✅ Verification

Once everything is installed, verify your setup:

- ✨ VS Code shows the Copilot icon in the status bar
- 🔄 CLI responds to `copilot` command
- 🔑 Authentication is successful
- 💬 You can interact with Copilot in both environments

---

## 🆘 Need Help?

If you encounter any issues during setup:
- Check the [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- Verify your internet connection
- Ensure you have the latest versions installed
- Contact your workshop instructor for assistance