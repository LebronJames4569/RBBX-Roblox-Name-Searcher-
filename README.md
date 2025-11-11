# RBBX (Roblox Name Searcher) - Description

RBBX is a powerful and user-friendly Roblox username availability checker tool that helps users find available usernames on the Roblox platform. 

## Key Features:

- **Automated Username Generation**: Generates random usernames with customizable length (minimum 3 characters)
- **Real-time Availability Checking**: Instantly checks if generated usernames are available on Roblox
- **Customizable Settings**: 
  - Adjustable username length
  - Configurable birthday format (for age verification)
  - Custom output filename for saving results
- **User-Friendly Interface**: 
  - Beautiful ASCII art introduction
  - Centered, box-style menu system
  - Color-coded output (green theme for available, red for taken usernames)
- **Performance Metrics**: Tracks checking speed, total attempts, and time elapsed
- **Rate Limit Handling**: Automatically manages Roblox API rate limits
- **Results Export**: Automatically saves available usernames to a text file

## How It Works:

1. Generates random usernames using lowercase letters and digits
2. Sends requests to Robox's validation API with proper headers
3. Analyzes response codes to determine availability
4. Immediately saves available usernames and provides visual feedback
5. Continues searching until it finds an available username or is stopped by the user

## Technical Details:

- Built with Python using requests library
- Cross-platform compatibility (Windows, macOS, Linux)
- Proper error handling for network issues and API limits
- Clean, organized code structure with global configuration options

Perfect for Roblox enthusiasts looking to find unique, available usernames quickly and efficiently!
