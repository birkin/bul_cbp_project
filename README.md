[![BUL Code Best-Practices](https://library.brown.edu/good_code/project_image/best-practices/)](https://library.brown.edu/good_code/project_info/best-practices/)


#### on this page...

- overview
- purpose
- inspiration
- features
- possibilities


#### overview

This is a django webapp that manages localized code-best-practices checks. Its three primary functions:

- It serves out a dynamically-updated score-badge which can be embedded in a version-control readme page (or elsewhere).

- It provides public and authorized-user views of the underlying data that produces the badge score.

- It enables automated reminder to-do emails to project owners.

- It provides a lightweight admin for authorized-users to edit an existing project's best-practices checklist or create a new-project checklist.


#### purpose

With experience, one's sense of what it takes for a _quality_ project to be _finished_ grows, with awareness of the constellation of ancillary best-practices. Some examples of these of best-practices...

- version code; make it public if possible
- if there’s a reasonable chance prepared data might be re-usable, deliver it via a webservice or installable library
- ensure web-resources have fluid displays for differing devices
- check accessibility
- rotate logs
- when patron data is captured, build in time-triggered deletion or anonymizing scripts
- ensure all library resources are discoverable by our discovery app
- offer data-feeds where appropriate
- configure apache to only use https
- ensure project’s readme has code/domain email contacts
- automate django session-db deletion
- add site-checker entry
- shib-protect admin urls
- etc.

So, the question, how to track these best-practice checks? And how to do this in a way that potentially invites a team approach?

One failed seemingly-good solution: a google spreadsheet where rows are projects, and columns are checklist-categories (the alternate would work too). The idea: team-members could add their projects to the checklist-spreadsheet, and then check off the categories (Yes/No/Not-Applicable) -- and if we wanted to, we could add programming to gather stats or generate reminder-triggers.

The problem with this was that it was _another-thing-to-do_ -- the checklist tracker was removed from the code and thus easy to forget about.

That's the nice thing about this approach -- the tracker is directly connected to the code repository, and it's right in the developer's face. A single markdown line at the top of the project's readme generates this html:

        <a href="https://library.brown.edu/bul_cbp/project_info/best-practices/">
            <img alt="BUL Code Best-Practices" src="https://library.brown.edu/bul_cbp/project_image/best-practices/" />
        </a>

(Here `best-practices` is a stub generated by the webapp.) So the default-github page of the project displays a badge with the project's score and a color (which is great because we take pride in good work) -- and the badge itself is a link to the checklist, thereby making the code-quality tracking process inviting and easy.


#### usage

- From the project's root info page, click 'Admin' and you'll be at the tracker admin page.
- Create a new entry, and fill it out. Note the `stub`, near the top.
- Save the entry via the `Save` button near the bottom-right.
- Go to the project's info-url, which will be in the form of `https://library.brown.edu/bul_cbp/project_info/the-stub/`
    - this page will show the calculated score, as well as the publicly viewable entries.
- If you're satisfied, to create a badge:
    - add this markdown to the top of your project's readme...

            [![BUL Code Best-Practices](https://library.brown.edu/bul_cbp/project_image/the-stub/)](https://library.brown.edu/bul_cbp/project_info/the-stub/)

#### inspiration

Credit...

Learning [Go](https://golang.org) a while back, I came across a [github project](https://github.com/syncthing/syncthing/blob/master/README.md) loaded with badges, one of which was `cli best practices / passing`. Clicking on that badge out of curiosity, and seeing that it was essentially a user-filled-out form, was initially underwhelming. I wondered if it was some lightweight way to inflate one's list of badges. But then I realized it was a potentially terrific way to manage the display and administration of the checklist idea I'd long had. Hence this experiment.


#### features

This is new, under-development outside of regular sprint-work, but implemented...

- dynamic color
    - green for high, yellow or red below certain thresholds
- incorporates time
    - why: software changes. You may be using the latest stable release of something now, but over six months there could be multiple security-releases of a foundational library your software uses. So when the badge loads, it reduces your score if a significant amount of time as passed for a given check.
- public / non-public info
    - why: publicly displaying the lack of an accessibility check won't compromise security, but there may well be incomplete-checks that you don't want advertised.
- django-admin filters to look at projects by categories


#### possibilities

- monthly summary emails to developers of to-dos
    - these could include both things not-done, and things that need to be re-checked due to the passage of time

- more dynamic scoring
    - right now it's simple: the score is simply the ratio of the sum of each completed entry, over the sum of each relevant (non "not-applicable") entry. But weighting could be applied to different checklist elements.

---

