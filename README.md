# Secure Remote Desktop Connection (Secure RDC)

This Python program provides a robust solution for managing Remote Desktop Connection (RDC) credentials and traces on Windows operating systems, enhancing your privacy and security. It empowers users to control and sanitize their remote desktop connections efficiently.

![securerdc](https://github.com/alasgarovs/Secure-RDC/assets/70092601/24419a65-fe55-45e8-b55f-b6aabf679f5f)


### Features

- **Credential Management:** Easily store and manage RDP login information using Windows generic credentials.
- **Connection Establishment:** Initiate remote desktop connections effortlessly with the provided credentials.
- **Trace Removal:** Clear all traces of the remote desktop connection for enhanced security and privacy.

### How it works?

- Sets up credentials for the specified IP address with the provided username and password.
- Launches a Remote Desktop Connection to the specified IP address.
- After the connection is finished, deletes stored credentials for the specified IP address.
- Removes terminal credentials associated with the specified IP address.
- Clears Terminal Server Client settings for a clean slate.
- Deletes the hidden Default.rdp file from the user's Documents directory.
- Deletes the non-hidden Default.rdp file from the user's Documents directory.

### Usage Guidelines

- Save your credentials using the provided script.
- Connect to the remote computer using the Windows Remote Desktop Connection program.
- For enhanced security, delete traces of the connection as needed.

**Note:** Ensure you have the necessary permissions before executing these commands.

Feel free to contribute, report issues, or suggest improvements!
