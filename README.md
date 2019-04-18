# python_netonix_api
Python class to access Netonix® WISP Switch WebAPI

**NEITHER THIS CODE NOR THE AUTHOR IS ASSOCIATED WITH NETONIX® IN ANY WAY.**
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

# Description
The Netonix® WISP Switches provide a WebAPI as backend for their webinterface. This python script allows to access this API directly.

Current methods:
```open(ip,user,password)
getConfig()
backup()
getMAC()
getStatus()
```
Not tested:
```putConfig()
restore()
```

to change configuration, you need to fetch the full configuratoin first, change it and push it back up:
```
	n=Netonix()
	n.open(ip,user,pw)
	n.getConfig()
	n.config['Switch_Name']="Switch-55"
	n.putConfig()

```  
