# Remote Desktop Privacy and Secure RDC

## Why Privacy matters in Remote Desktop Connections

In an era where remote work and connectivity are more prevalent than ever, ensuring the privacy and security of remote desktop connections is paramount. Unauthorized access, data breaches, and traces of sensitive information can pose serious risks.

## Secure Remote Desktop Connection (Secure RDC)

This Python program provides a robust solution for managing Remote Desktop Connection (RDC) credentials and traces on Windows operating systems, enhancing your privacy and security. It empowers users to control and sanitize their remote desktop connections efficiently.

### Features

- **Credential Management:** Easily store and manage RDP login information using Windows generic credentials.
- **Connection Establishment:** Initiate remote desktop connections effortlessly with the provided credentials.
- **Trace Removal:** Clear all traces of the remote desktop connection for enhanced security and privacy.

### How it works?

1. Sets up credentials for the specified IP address with the provided username and password.
2. Launches a Remote Desktop Connection to the specified IP address.
3. After the connection is finished, deletes stored credentials for the specified IP address.
4. Removes terminal credentials associated with the specified IP address.
5. Clears Terminal Server Client settings for a clean slate.
6. Deletes the hidden Default.rdp file from the user's Documents directory.
7. Deletes the non-hidden Default.rdp file from the user's Documents directory.

### Usage Guidelines

- Save your credentials using the provided script.
- Connect to the remote computer using the Windows Remote Desktop Connection program.
- For enhanced security, delete traces of the connection as needed.

**Note:** Ensure you have the necessary permissions before executing these commands.

Feel free to contribute, report issues, or suggest improvements!
