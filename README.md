# CLI-Based Image Registration and Search System

This project is a command-line interface (CLI) application that allows users to register images, search for matching images, and deregister images using a relational database.

The application uses perceptual hashing to detect visually similar images rather than relying on exact file matches.

---

## Features

- Register images with a name
- Search database using an input image
- Prevent false positives using similarity threshold
- De-register images by name or ID
- List all registered images
- SQLite-based relational database
- Virtual environment support

---

## Installation & Setup

### 1. Create virtual environment

python -m venv venv

### 2. Activate the Virtual Environment

<pre class="overflow-visible! px-0!" data-start="351" data-end="436"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span># Windows</span><span>
venv\Scripts\activate

</span><span># macOS / Linux</span><span>
</span><span>source</span><span> venv/bin/activate
</span></span></code></div></div></pre>

### 3. Install Dependencies

<pre class="overflow-visible! px-0!" data-start="466" data-end="509"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
</span></span></code></div></div></pre>

---

## Project Structure

<pre class="overflow-visible! px-0!" data-start="538" data-end="838"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>project_folder/
│
├── venv/
├── main.py          </span><span># Application entry point</span><span>
├── cli.py           </span><span># CLI argument parsing</span><span>
├── database.py      </span><span># Database & image hashing logic</span><span>
├── db_view.py       </span><span># Database inspection logic</span><span>
├── image_db.sqlite  </span><span># SQLite relational database</span><span>
├── requirements.txt
</span></span></code></div></div></pre>

---

## How the Application Works

The application is a CLI-based image registration and search system backed by a relational database.

### Core Workflow

1. Images are registered with a name via CLI.
2. Each image is converted into a  **perceptual hash (pHash)** .
3. Image metadata and hash are stored in an SQLite database.
4. Search operations compare perceptual hashes using  **Hamming distance** .
5. A similarity threshold prevents false-positive matches.
6. Images can be safely de-registered using name or ID.

---

## CLI Commands

### Register an Image

<pre class="overflow-visible! px-0!" data-start="1400" data-end="1469"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python main.py register --name Dog --image path/to/query_image.jpg
</span></span></code></div></div></pre>

Stores the image metadata and perceptual hash in the database.

---

### Search for a Matching Image

<pre class="overflow-visible! px-0!" data-start="1572" data-end="1630"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python main.py search --image path/to/query_image.jpg
</span></span></code></div></div></pre>

If a similar image exists within the threshold:

<pre class="overflow-visible! px-0!" data-start="1680" data-end="1720"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>🔍 </span><span>Match</span><span> found: Dog (distance</span><span>=</span><span>3</span><span>)
</span></span></code></div></div></pre>

If no valid match exists:

<pre class="overflow-visible! px-0!" data-start="1748" data-end="1803"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>❌ </span><span>No</span><span> matching image </span><span>found</span><span> (closest distance=</span><span>24</span><span>)
</span></span></code></div></div></pre>

Optional threshold override:

<pre class="overflow-visible! px-0!" data-start="1834" data-end="1906"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python main.py search --image images/query.jpg --threshold 8
</span></span></code></div></div></pre>

---

### List All Registered Images

<pre class="overflow-visible! px-0!" data-start="1944" data-end="1975"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python main.py list
</span></span></code></div></div></pre>

Example output:

<pre class="overflow-visible! px-0!" data-start="1993" data-end="2082"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>ID:</span><span></span><span>3</span><span></span><span>|</span><span></span><span>Name:</span><span></span><span>Dog</span><span></span><span>|</span><span></span><span>Path:</span><span></span><span>images/dog.jpg</span><span>
</span><span>ID:</span><span></span><span>4</span><span></span><span>|</span><span></span><span>Name:</span><span></span><span>Cat</span><span></span><span>|</span><span></span><span>Path:</span><span></span><span>images/cat.jpg</span><span>
</span></span></code></div></div></pre>

---

### De-register an Image by Name

<pre class="overflow-visible! px-0!" data-start="2122" data-end="2170"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python main.py deregister --name Dog
</span></span></code></div></div></pre>

---

### De-register an Image by ID

<pre class="overflow-visible! px-0!" data-start="2208" data-end="2252"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python main.py deregister --</span><span>id</span><span> 3
</span></span></code></div></div></pre>

---

## Image Matching Logic

* Uses **perceptual hashing (pHash)** instead of cryptographic hashing
* Supports detection of visually similar images
* Hamming distance determines similarity
* Default similarity threshold prevents false positives
* Images not present in the database are safely rejected

---

## Database Design Notes

* Uses SQLite as a relational database
* Image IDs are auto-incremented and not reused after deletion
* Database stores metadata and hashes, not image files
* Deleted rows do not waste disk space

---

## Key Design Decisions

* Separation of concerns (CLI, DB logic, entry point)
* Safe default similarity threshold
* Consistent return values to avoid runtime errors
* Support for de-registration via both name and primary key ID
* Read-only database inspection command

---

## Conclusion

This project demonstrates a complete CLI-based system for image registration, perceptual image matching, and safe de-registration using Python and SQLite. It handles real-world edge cases such as false positives, accidental deletions, and database consistency while maintaining a clean and extensible design.

<pre class="overflow-visible! px-0!" data-start="3390" data-end="3739" data-is-last-node=""><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"></div></div></pre>
