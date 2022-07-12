var StyleInjector = {
    inject: (path, mid) => {
        document.documentElement.setAttribute("mid", mid)

        forEditorField([], (field) => {
            let editable = field.editingArea.editable
            editable.setAttribute("mid", mid)

            if (!field.hasAttribute("has-css-injected")) {
                editable.classList.add(...document.body.classList)

                let link = document.createElement("link")
                link.href = path
                link.type = "text/css"
                link.rel = "stylesheet"

                editable.getRootNode().insertBefore(link, editable)
                field.setAttribute("has-css-injected", "")
            }
        })
    }
}
