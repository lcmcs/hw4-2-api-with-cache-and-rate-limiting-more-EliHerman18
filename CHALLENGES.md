**Challenge 1: Tracking Cache Hits for the Bonus Loop**
Originally I was trying to check 
`if len(citys_set) < len(citys_set.add(city.lower()))`
and if it was I would up `api_citys` and add `city.lower()`
to the set else up `cached_citys`. But `len(citys_set.add(city.lower()))`
was throwing an error, and I'm still not entirely why I don't 
know sets so well. While looking at other parts of my code 
I remember I can just check if something is in it. and at this
point in write this I realized it could be a list, so I switched it.

**Challenge 2: Implementing the Cache correctly**
Initially I didn't realize we were supposed to do
in-memory cache, I overcomplicated the caching 
requirement by building a system that read and wrote
cache data to a physical `api_cache.json` file.
While it worked, it was unnecessary for the scope 
of the assignment. I simplified the code by switching
to an "in-memory" cache, using a global dictionary
`CACHE = {}` at the top of my code. This made retrieving 
previously searched cities instantaneous and cleaned
up my codebase significantly as well as resting the cache 
every time the code was run.