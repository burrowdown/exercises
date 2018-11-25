# Bank exercise

Completed for AltSource on 11/24/2018

If I was going to keep going, I would:
* Finish unit tests, currently only Account is tested. (It's not a coincidence that that's the only module with all the user input factored out!)
* Clean up the UI for consistency and readability.
* Add a uniqueness constraint for account IDs, (though maybe that wants to wait for a database.)
* Reimplement through a web interface using Vue.js.

### Prompt

"You have been tasked with writing the world’s greatest banking ledger. Please code a solution that can perform the following workflows through a console application (accessed via the command line):

-Create a new account
-Login
-Record a deposit
-Record a withdrawal
-Check balance
-See transaction history
-Log out

For additional credit, you may implement this through a web page. They don’t have to run at the same time, but if you would like to do that, feel free.

C# is preferred but not required. Use whatever frameworks/libraries you wish, and just make sure they are included or available via via NuGet/npm/etc. Please use a temporary memory store (local cache) instead of creating an actual database, and don't spend much time on the UI (unless you love doing that)."
