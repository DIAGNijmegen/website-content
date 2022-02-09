# Content tags

To make writing content easier, custom tags can be used to include special content.

## Embedding YouTube/vimeo movies

`[youtube: <video id>]`

Example: [youtube: 9ks7cLpYAw8]

`[vimeo: <video id>]`

Example: [vimeo: 326352382]

Adds an embedded and responsive YouTube/vimeo frame to a page.

## Linking to content pages

`[<content type>/<slug>]`

Examples:

- `[member/wouter-bulten]`
- `[software/asap]`
- `[vacancy/deep-learning-for-artifacts]`
- `[project/deeppca]`
- `[presentation/unsupervised-prostate-cancer-detection]`

Creates a link to the member page of that user on the correct website.

`[<content type>/<slug>, group: <group>]`

Example `[member/wouter-bulten, group: pathology]`

Creates a link to a page on a specific website.

## Linking to Grand-Challenge

`[grandchallenge/identifier, slug: slug]`

Examples:

- `[grandchallenge/archives, slug: luna16]`
- `[grandchallenge/algorithms, slug: gleason-grading-of-prostate-biopsies]`

Creates a card with image and description matched to grand challenge. Note only public access can linked
To create a row of cards, surround multiple special grand challenge tags in a row div, e.g.,:
```
    <div class=row>
    [grandchallenge/archives, slug: luna16]
    [grandchallenge/algorithms, slug: gleason-grading-of-prostate-biopsies]
    </div>
```
