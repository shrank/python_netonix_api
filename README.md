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


to change configuration, you need to fetch the full configuration first, change it and push it back up:
```
from netonix_api import Netonix

	n=Netonix()
	n.open(ip,user,pw)
	n.getConfig()
	n.config['Switch_Name']="Switch-55"
	n.putConfig()

```  
