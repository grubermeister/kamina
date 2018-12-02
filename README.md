### Description of submodules:

* kamina-script:
	* stackless - Stackless Python 2.7-slp
		> used to bootstrap a basic application VM, will eventually be
		replaced by a register-based VM, simple to port to new platforms
		
	* pypy - Python in Python
		> used to demonstrate language implementation on top of the 
		generic application VM.  Must be ported to the replacement VM
		
	* topaz - Ruby in Python
		> used to demonstrate alternative language implementation on top 
		of the generic VM.  Must be comparative in performance to other
		languages implemented on the platform, providing certain 
		guarantees to platform developers
		
* kamina-hmdp:
	> A fork of the Python implementation of the Kademlia Dyanamic Hash
	Table.  Rather than being based on a variant of XML-RPC, the Hyper-
	Media Distribution Protocol will implement a superset of HTTP
	defined by RFC 5322 [https://tools.ietf.org/html/rfc5322].  Will 
	eventually implement DTLS for cryptographic handshakes, but 
	communications facilitated by a variant of PGP instead of the SSL
	PKI.  This protocol will also allow for domain name resolution, by
	passing domain information amongst DHT participants; think of
	DNS records here as more .torrent files than BIND records. 
	
* kamina-pkg:
	> An AUR-influenced packaging system for Kamina applications, which 
	will validate package contents via the PGP key system, and retrieve 
	package contents organized in Git repositories, their contents 
	distributed via kamina-hmdp.  Kamina applications are written using
	a language implemented under kamina-script.
	
* kamina-gui:
	> Think of this one as simplified, performant Electron.  The DOM will
	be implemented with a Smalltalk object structure, app layouts
	defined by a markup such as YAML, JSON, or TOML.
---	
### So, what is this repo?
	
	The basic kamina repo ties all of these modules together to 
	implement what you would consider akin to a web browser. You choose
	your language implemented under kamina-script, you build the GUI on
	top of kamina-gui, bundle as a kamina-pkg, and distribute it all 
	with kamina-hmdp.  This repo will also include a basic graphical
	front-end for kamina-pkg, and allow things such as bookmarks,
	history, caching, user profiles, etc.
