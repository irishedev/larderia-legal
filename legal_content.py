"""Localized legal page content for Larderia (privacy policy and account deletion)."""

PRIVACY_PAGES = {
    "en":     {
        "html_lang": "en",
        "title": "Larderia Privacy Policy",
        "updated": "Last updated: June 21, 2026",
        "sections": [
            {
                "heading": "Overview",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Cairn Studio (&ldquo;we&rdquo;, &ldquo;us&rdquo;) operates the Larderia mobile app. "
                            "Larderia helps households track food inventory. You may use the app without an account "
                            "(data stays on your device) or create an account to sync data across devices and share "
                            "with a household.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>Contact: <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
            {
                "heading": "Information we collect",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Account information</strong> &mdash; email address and optional display name when you sign up.",
                            "<strong>Inventory data</strong> &mdash; items, quantities, storage locations, consumption and waste logs, categories, allergens, and nutrition preferences you enter.",
                            "<strong>Household data</strong> &mdash; household name, address (if you provide it), member roles, and managed dependent profiles.",
                            "<strong>Camera (optional)</strong> &mdash; used only for barcode scanning and on-device text recognition (nutrition labels, receipts). Images are processed on your device and are not uploaded to our servers in version 1.0.",
                            "<strong>Product images</strong> &mdash; when you scan a barcode, we may display a product thumbnail URL from Open Food Facts; we do not store that image on our servers.",
                            "<strong>Push notifications</strong> &mdash; device tokens so we can send reminder notifications you enable.",
                            "<strong>Health data (optional)</strong> &mdash; if you opt in, nutrition information from logged consumption may be written to Apple Health or Health Connect on your device.",
                            "<strong>Location (optional)</strong> &mdash; used only to help set your household address when you choose to use that feature.",
                        ],
                    },
                ],
            },
            {
                "heading": "How we use information",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>We use this data to provide inventory tracking, household sharing, reports, "
                            "reminders, and optional health export. We do not sell your personal information.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Where data is stored",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Local-only mode</strong> &mdash; data is stored on your device. Your operating system may include app data in device backups (for example iCloud Backup or Android Auto Backup).",
                            "<strong>Cloud accounts</strong> &mdash; data is stored in Google Firebase (Firestore) in access-controlled databases. Authentication is handled by Firebase Auth. Version 1.0 does not upload user photos to Firebase Cloud Storage.",
                        ],
                    },
                ],
            },
            {
                "heading": "Crash, diagnostics, performance, and analytics",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>In release builds we use <strong>Google Firebase Crashlytics</strong> to collect "
                            "crash reports and limited diagnostic events (for example sync or push registration "
                            "failures). Reports may include your Firebase account id, app version, device type, and "
                            "locale. We do not include inventory contents, household names, email addresses, or "
                            "notification tokens in these reports. Crash collection is disabled while you run a debug "
                            "build from Xcode or Android Studio.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>We also use <strong>Google Firebase Performance Monitoring</strong> to measure app "
                            "startup time and the duration of selected operations (for example sync queue replay). "
                            "Performance data may include device type, app version, and coarse timing metrics. It "
                            "does not include inventory contents or personal identifiers beyond your Firebase account "
                            "id. Performance collection is disabled in debug builds.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>When you are signed in to a cloud account (not in local-only mode), we use "
                            "<strong>Google Firebase Analytics</strong> in release builds to understand how the app "
                            "is used &mdash; for example which main screens you open and when you sign in, sign up, "
                            "sign out, or delete your account. Analytics may include your Firebase account id, app "
                            "version, device type, locale, and coarse interaction events. We do not send inventory "
                            "contents, household names, email addresses, item names, or barcode numbers to Analytics. "
                            "Analytics collection is disabled in debug builds and when you use the app without a "
                            "cloud account.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Third-party services",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Google Firebase</strong> &mdash; authentication, cloud database, push notifications, cloud functions, crash/diagnostics reporting, performance monitoring, and usage analytics (when signed in to a cloud account).",
                            "<strong>Open Food Facts</strong> &mdash; barcode product lookups. We send barcode numbers to look up product information; we do not send your inventory lists.",
                        ],
                    },
                ],
            },
            {
                "heading": "Data retention and deletion",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>We retain your data while your account is active. When not signed in to the cloud, "
                            "you may export local data from Settings.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Households you own are deleted for all members, who are notified. If you belong to "
                            "another household as a member or admin, you are removed and the owner is notified.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>To delete your cloud account and associated data, follow the steps on our <a "
                            "href=\"{delete_account_url}\">account deletion request page</a>, use <strong>Settings "
                            "&rarr; Account &rarr; Delete account</strong> in the app, or email <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a> from your registered "
                            "email address.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Children&rsquo;s privacy",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Larderia is not directed to children under 13. We do not knowingly collect personal "
                            "information from children under 13.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Changes",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>We may update this policy from time to time. The &ldquo;Last updated&rdquo; date at "
                            "the top of this page will change when we do.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Contact",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Questions about this policy: <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>"
                        ),
                    },
                ],
            },
        ],
    },
    "de":     {
        "html_lang": "de",
        "title": "Datenschutzerklärung für Larderia",
        "updated": "Zuletzt aktualisiert: 21. Juni 2026",
        "sections": [
            {
                "heading": "Überblick",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Cairn Studio (&bdquo;wir&ldquo;, &bdquo;uns&ldquo;) betreibt die mobile App Larderia. "
                            "Larderia hilft Haushalten, den Lebensmittelbestand zu verwalten. Sie können die App ohne "
                            "Konto nutzen (Daten bleiben auf Ihrem Gerät) oder ein Konto erstellen, um Daten "
                            "geräteübergreifend zu synchronisieren und mit einem Haushalt zu teilen.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>Kontakt: <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
            {
                "heading": "Welche Informationen wir erheben",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Kontoinformationen</strong> &mdash; E-Mail-Adresse und optionaler Anzeigename bei der Registrierung.",
                            "<strong>Bestandsdaten</strong> &mdash; Artikel, Mengen, Lagerorte, Verbrauchs- und Abfallprotokolle, Kategorien, Allergene und Ernährungspräferenzen, die Sie eingeben.",
                            "<strong>Haushaltsdaten</strong> &mdash; Haushaltsname, Adresse (falls angegeben), Mitgliederrollen und verwaltete Profile abhängiger Personen.",
                            "<strong>Kamera (optional)</strong> &mdash; nur für Barcode-Scans und Texterkennung auf dem Gerät (Nährwertetiketten, Belege). Bilder werden auf Ihrem Gerät verarbeitet und in Version 1.0 nicht auf unsere Server hochgeladen.",
                            "<strong>Produktbilder</strong> &mdash; beim Scannen eines Barcodes können wir eine Produktminiatur-URL von Open Food Facts anzeigen; wir speichern dieses Bild nicht auf unseren Servern.",
                            "<strong>Push-Benachrichtigungen</strong> &mdash; Gerätetoken, damit wir Erinnerungsbenachrichtigungen senden können, die Sie aktivieren.",
                            "<strong>Gesundheitsdaten (optional)</strong> &mdash; wenn Sie zustimmen, können Nährwertinformationen aus protokolliertem Verbrauch in Apple Health oder Health Connect auf Ihrem Gerät gespeichert werden.",
                            "<strong>Standort (optional)</strong> &mdash; nur zur Unterstützung beim Festlegen Ihrer Haushaltsadresse, wenn Sie diese Funktion nutzen.",
                        ],
                    },
                ],
            },
            {
                "heading": "Wie wir Informationen verwenden",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Wir verwenden diese Daten, um Bestandsverwaltung, Haushaltsfreigabe, Berichte, "
                            "Erinnerungen und optionalen Gesundheitsexport bereitzustellen. Wir verkaufen Ihre "
                            "personenbezogenen Daten nicht.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Wo Daten gespeichert werden",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Nur-lokal-Modus</strong> &mdash; Daten werden auf Ihrem Gerät gespeichert. Ihr Betriebssystem kann App-Daten in Gerätesicherungen einbeziehen (z.&nbsp;B. iCloud-Backup oder Android Auto Backup).",
                            "<strong>Cloud-Konten</strong> &mdash; Daten werden in Google Firebase (Firestore) in zugriffsgeschützten Datenbanken gespeichert. Die Authentifizierung erfolgt über Firebase Auth. Version 1.0 lädt keine Benutzerfotos in Firebase Cloud Storage hoch.",
                        ],
                    },
                ],
            },
            {
                "heading": "Abstürze, Diagnose, Leistung und Analysen",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>In Release-Builds verwenden wir <strong>Google Firebase Crashlytics</strong>, um "
                            "Absturzberichte und begrenzte Diagnoseereignisse zu erfassen (z.&nbsp;B. "
                            "Synchronisierungs- oder Push-Registrierungsfehler). Berichte können Ihre "
                            "Firebase-Konto-ID, App-Version, Gerätetyp und Gebietsschema enthalten. Bestandsinhalte, "
                            "Haushaltsnamen, E-Mail-Adressen oder Benachrichtigungstoken sind nicht enthalten. Die "
                            "Absturzerfassung ist deaktiviert, wenn Sie einen Debug-Build aus Xcode oder Android "
                            "Studio ausführen.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Wir verwenden außerdem <strong>Google Firebase Performance Monitoring</strong>, um "
                            "die App-Startzeit und die Dauer ausgewählter Vorgänge zu messen (z.&nbsp;B. Wiedergabe "
                            "der Synchronisierungswarteschlange). Leistungsdaten können Gerätetyp, App-Version und "
                            "grobe Zeitmetriken umfassen. Sie enthalten keine Bestandsinhalte oder personenbezogenen "
                            "Kennungen außer Ihrer Firebase-Konto-ID. Die Leistungserfassung ist in Debug-Builds "
                            "deaktiviert.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Wenn Sie bei einem Cloud-Konto angemeldet sind (nicht im Nur-lokal-Modus), verwenden "
                            "wir in Release-Builds <strong>Google Firebase Analytics</strong>, um zu verstehen, wie "
                            "die App genutzt wird &mdash; z.&nbsp;B. welche Hauptbildschirme geöffnet werden und wann "
                            "Sie sich anmelden, registrieren, abmelden oder Ihr Konto löschen. Analysen können Ihre "
                            "Firebase-Konto-ID, App-Version, Gerätetyp, Gebietsschema und grobe "
                            "Interaktionsereignisse umfassen. Bestandsinhalte, Haushaltsnamen, E-Mail-Adressen, "
                            "Artikelnamen oder Barcodes senden wir nicht an Analytics. Die Analyseerfassung ist in "
                            "Debug-Builds und bei Nutzung ohne Cloud-Konto deaktiviert.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Dienste Dritter",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Google Firebase</strong> &mdash; Authentifizierung, Cloud-Datenbank, Push-Benachrichtigungen, Cloud Functions, Absturz-/Diagnoseberichte, Leistungsüberwachung und Nutzungsanalysen (bei Anmeldung mit Cloud-Konto).",
                            "<strong>Open Food Facts</strong> &mdash; Barcode-Produktabfragen. Wir senden Barcode-Nummern zur Produktinformation; Ihre Bestandslisten senden wir nicht.",
                        ],
                    },
                ],
            },
            {
                "heading": "Datenspeicherung und -löschung",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Wir speichern Ihre Daten, solange Ihr Konto aktiv ist. Ohne Cloud-Anmeldung können "
                            "Sie lokale Daten unter <strong>Einstellungen</strong> exportieren.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Haushalte, die Ihnen gehören, werden für alle Mitglieder gelöscht; diese werden "
                            "benachrichtigt. Gehören Sie einem anderen Haushalt als Mitglied oder Administrator an, "
                            "werden Sie entfernt und der Eigentümer wird benachrichtigt.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Um Ihr Cloud-Konto und zugehörige Daten zu löschen, folgen Sie den Schritten auf "
                            "unserer <a href=\"{delete_account_url}\">Seite zur Kontolöschung</a>, nutzen Sie "
                            "<strong>Einstellungen &rarr; Konto &rarr; Konto löschen</strong> in der App oder senden "
                            "Sie eine E-Mail an <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a> von Ihrer "
                            "registrierten E-Mail-Adresse.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Datenschutz für Kinder",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Larderia richtet sich nicht an Kinder unter 13 Jahren. Wir erheben wissentlich keine "
                            "personenbezogenen Daten von Kindern unter 13 Jahren.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Änderungen",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Wir können diese Richtlinie von Zeit zu Zeit aktualisieren. Das Datum &bdquo;Zuletzt "
                            "aktualisiert&ldquo; oben auf dieser Seite ändert sich entsprechend.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Kontakt",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Fragen zu dieser Richtlinie: <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>"
                        ),
                    },
                ],
            },
        ],
    },
    "es":     {
        "html_lang": "es",
        "title": "Política de privacidad de Larderia",
        "updated": "Última actualización: 21 de junio de 2026",
        "sections": [
            {
                "heading": "Resumen",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Cairn Studio (&laquo;nosotros&raquo;, &laquo;nos&raquo;) opera la aplicación móvil "
                            "Larderia. Larderia ayuda a los hogares a gestionar el inventario de alimentos. Puede "
                            "usar la app sin cuenta (los datos permanecen en su dispositivo) o crear una cuenta para "
                            "sincronizar datos entre dispositivos y compartirlos con un hogar.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>Contacto: <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
            {
                "heading": "Información que recopilamos",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Información de la cuenta</strong> &mdash; dirección de correo electrónico y nombre para mostrar opcional al registrarse.",
                            "<strong>Datos de inventario</strong> &mdash; artículos, cantidades, ubicaciones de almacenamiento, registros de consumo y desperdicio, categorías, alérgenos y preferencias nutricionales que introduzca.",
                            "<strong>Datos del hogar</strong> &mdash; nombre del hogar, dirección (si la proporciona), roles de los miembros y perfiles de dependientes gestionados.",
                            "<strong>Cámara (opcional)</strong> &mdash; solo para escanear códigos de barras y reconocimiento de texto en el dispositivo (etiquetas nutricionales, recibos). Las imágenes se procesan en su dispositivo y no se suben a nuestros servidores en la versión 1.0.",
                            "<strong>Imágenes de productos</strong> &mdash; al escanear un código de barras, podemos mostrar una miniatura del producto desde Open Food Facts; no almacenamos esa imagen en nuestros servidores.",
                            "<strong>Notificaciones push</strong> &mdash; tokens del dispositivo para enviar recordatorios que active.",
                            "<strong>Datos de salud (opcional)</strong> &mdash; si lo acepta, la información nutricional del consumo registrado puede escribirse en Apple Health o Health Connect en su dispositivo.",
                            "<strong>Ubicación (opcional)</strong> &mdash; solo para ayudar a establecer la dirección de su hogar cuando elija usar esa función.",
                        ],
                    },
                ],
            },
            {
                "heading": "Cómo usamos la información",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Usamos estos datos para ofrecer seguimiento de inventario, uso compartido en el "
                            "hogar, informes, recordatorios y exportación opcional de datos de salud. No vendemos su "
                            "información personal.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Dónde se almacenan los datos",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Modo solo local</strong> &mdash; los datos se almacenan en su dispositivo. Su sistema operativo puede incluir los datos de la app en copias de seguridad del dispositivo (por ejemplo, copia de seguridad de iCloud o Android Auto Backup).",
                            "<strong>Cuentas en la nube</strong> &mdash; los datos se almacenan en Google Firebase (Firestore) en bases de datos con control de acceso. La autenticación la gestiona Firebase Auth. La versión 1.0 no sube fotos de usuario a Firebase Cloud Storage.",
                        ],
                    },
                ],
            },
            {
                "heading": "Fallos, diagnóstico, rendimiento y analítica",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>En versiones de producción usamos <strong>Google Firebase Crashlytics</strong> para "
                            "recopilar informes de fallos y eventos de diagnóstico limitados (por ejemplo, fallos de "
                            "sincronización o registro push). Los informes pueden incluir su id de cuenta de "
                            "Firebase, versión de la app, tipo de dispositivo y configuración regional. No incluimos "
                            "contenidos del inventario, nombres de hogares, direcciones de correo ni tokens de "
                            "notificación. La recopilación de fallos está desactivada al ejecutar una compilación de "
                            "depuración desde Xcode o Android Studio.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>También usamos <strong>Google Firebase Performance Monitoring</strong> para medir el "
                            "tiempo de inicio de la app y la duración de operaciones seleccionadas (por ejemplo, "
                            "reproducción de la cola de sincronización). Los datos de rendimiento pueden incluir tipo "
                            "de dispositivo, versión de la app y métricas de tiempo aproximadas. No incluyen "
                            "contenidos del inventario ni identificadores personales más allá de su id de cuenta de "
                            "Firebase. La recopilación de rendimiento está desactivada en compilaciones de "
                            "depuración.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Cuando ha iniciado sesión en una cuenta en la nube (no en modo solo local), usamos "
                            "<strong>Google Firebase Analytics</strong> en versiones de producción para entender cómo "
                            "se usa la app &mdash; por ejemplo, qué pantallas principales abre y cuándo inicia "
                            "sesión, se registra, cierra sesión o elimina su cuenta. La analítica puede incluir su id "
                            "de cuenta de Firebase, versión de la app, tipo de dispositivo, configuración regional y "
                            "eventos de interacción generales. No enviamos contenidos del inventario, nombres de "
                            "hogares, correos electrónicos, nombres de artículos ni códigos de barras a Analytics. La "
                            "recopilación analítica está desactivada en compilaciones de depuración y cuando usa la "
                            "app sin cuenta en la nube.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Servicios de terceros",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Google Firebase</strong> &mdash; autenticación, base de datos en la nube, notificaciones push, funciones en la nube, informes de fallos/diagnóstico, supervisión del rendimiento y analítica de uso (con sesión iniciada en cuenta en la nube).",
                            "<strong>Open Food Facts</strong> &mdash; consultas de productos por código de barras. Enviamos números de código de barras para buscar información del producto; no enviamos sus listas de inventario.",
                        ],
                    },
                ],
            },
            {
                "heading": "Conservación y eliminación de datos",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Conservamos sus datos mientras su cuenta esté activa. Sin sesión en la nube, puede "
                            "exportar datos locales desde <strong>Ajustes</strong>.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Los hogares de su propiedad se eliminan para todos los miembros, que son notificados. "
                            "Si pertenece a otro hogar como miembro o administrador, se le elimina y se notifica al "
                            "propietario.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Para eliminar su cuenta en la nube y los datos asociados, siga los pasos en nuestra "
                            "<a href=\"{delete_account_url}\">página de solicitud de eliminación de cuenta</a>, use "
                            "<strong>Ajustes &rarr; Cuenta &rarr; Eliminar cuenta</strong> en la app o envíe un "
                            "correo a <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a> desde su "
                            "dirección registrada.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Privacidad de menores",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Larderia no está dirigida a menores de 13 años. No recopilamos a sabiendas "
                            "información personal de menores de 13 años.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Cambios",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Podemos actualizar esta política periódicamente. La fecha de &laquo;Última "
                            "actualización&raquo; en la parte superior de esta página cambiará cuando lo hagamos.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Contacto",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Preguntas sobre esta política: <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>"
                        ),
                    },
                ],
            },
        ],
    },
    "fr":     {
        "html_lang": "fr",
        "title": "Politique de confidentialité de Larderia",
        "updated": "Dernière mise à jour : 21 juin 2026",
        "sections": [
            {
                "heading": "Aperçu",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Cairn Studio (&laquo;&nbsp;nous&nbsp;&raquo;, &laquo;&nbsp;notre&nbsp;&raquo;) "
                            "exploite l&rsquo;application mobile Larderia. Larderia aide les foyers à suivre leur "
                            "inventaire alimentaire. Vous pouvez utiliser l&rsquo;application sans compte (les "
                            "données restent sur votre appareil) ou créer un compte pour synchroniser les données "
                            "entre appareils et les partager au sein d&rsquo;un foyer.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Contact&nbsp;: <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Informations que nous collectons",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Informations de compte</strong> &mdash; adresse e-mail et nom d&rsquo;affichage facultatif lors de l&rsquo;inscription.",
                            "<strong>Données d&rsquo;inventaire</strong> &mdash; articles, quantités, emplacements de stockage, journaux de consommation et de gaspillage, catégories, allergènes et préférences nutritionnelles que vous saisissez.",
                            "<strong>Données du foyer</strong> &mdash; nom du foyer, adresse (si vous la fournissez), rôles des membres et profils de personnes à charge gérés.",
                            "<strong>Appareil photo (facultatif)</strong> &mdash; utilisé uniquement pour la lecture de codes-barres et la reconnaissance de texte sur l&rsquo;appareil (étiquettes nutritionnelles, reçus). Les images sont traitées sur votre appareil et ne sont pas téléversées sur nos serveurs dans la version&nbsp;1.0.",
                            "<strong>Images de produits</strong> &mdash; lorsque vous scannez un code-barres, nous pouvons afficher une vignette produit depuis Open Food Facts&nbsp;; nous ne stockons pas cette image sur nos serveurs.",
                            "<strong>Notifications push</strong> &mdash; jetons d&rsquo;appareil pour envoyer les rappels que vous activez.",
                            "<strong>Données de santé (facultatif)</strong> &mdash; si vous y consentez, les informations nutritionnelles issues de la consommation enregistrée peuvent être écrites dans Apple Health ou Health Connect sur votre appareil.",
                            "<strong>Localisation (facultatif)</strong> &mdash; utilisée uniquement pour vous aider à définir l&rsquo;adresse de votre foyer lorsque vous choisissez d&rsquo;utiliser cette fonctionnalité.",
                        ],
                    },
                ],
            },
            {
                "heading": "Comment nous utilisons les informations",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Nous utilisons ces données pour fournir le suivi d&rsquo;inventaire, le partage au "
                            "sein du foyer, les rapports, les rappels et l&rsquo;exportation facultative vers les "
                            "apps de santé. Nous ne vendons pas vos informations personnelles.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Où les données sont stockées",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Mode local uniquement</strong> &mdash; les données sont stockées sur votre appareil. Votre système d&rsquo;exploitation peut inclure les données de l&rsquo;application dans les sauvegardes de l&rsquo;appareil (par exemple sauvegarde iCloud ou Android Auto Backup).",
                            "<strong>Comptes cloud</strong> &mdash; les données sont stockées dans Google Firebase (Firestore) dans des bases de données à accès contrôlé. L&rsquo;authentification est gérée par Firebase Auth. La version&nbsp;1.0 ne téléverse pas de photos utilisateur vers Firebase Cloud Storage.",
                        ],
                    },
                ],
            },
            {
                "heading": "Plantages, diagnostics, performances et analyses",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Dans les versions de production, nous utilisons <strong>Google Firebase "
                            "Crashlytics</strong> pour collecter des rapports de plantage et des événements de "
                            "diagnostic limités (par exemple échecs de synchronisation ou d&rsquo;enregistrement "
                            "push). Les rapports peuvent inclure votre identifiant de compte Firebase, la version de "
                            "l&rsquo;application, le type d&rsquo;appareil et la langue. Nous n&rsquo;y incluons pas "
                            "le contenu de l&rsquo;inventaire, les noms de foyer, les adresses e-mail ni les jetons "
                            "de notification. La collecte des plantages est désactivée lorsque vous exécutez une "
                            "version de débogage depuis Xcode ou Android Studio.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Nous utilisons également <strong>Google Firebase Performance Monitoring</strong> pour "
                            "mesurer le temps de démarrage de l&rsquo;application et la durée d&rsquo;opérations "
                            "sélectionnées (par exemple relecture de la file de synchronisation). Les données de "
                            "performance peuvent inclure le type d&rsquo;appareil, la version de l&rsquo;application "
                            "et des métriques de temps approximatives. Elles n&rsquo;incluent pas le contenu de "
                            "l&rsquo;inventaire ni d&rsquo;identifiants personnels au-delà de votre identifiant de "
                            "compte Firebase. La collecte de performance est désactivée dans les versions de "
                            "débogage.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Lorsque vous êtes connecté à un compte cloud (pas en mode local uniquement), nous "
                            "utilisons <strong>Google Firebase Analytics</strong> dans les versions de production "
                            "pour comprendre comment l&rsquo;application est utilisée &mdash; par exemple quels "
                            "écrans principaux vous ouvrez et quand vous vous connectez, vous inscrivez, vous "
                            "déconnectez ou supprimez votre compte. Les analyses peuvent inclure votre identifiant de "
                            "compte Firebase, la version de l&rsquo;application, le type d&rsquo;appareil, la langue "
                            "et des événements d&rsquo;interaction généraux. Nous n&rsquo;envoyons pas le contenu de "
                            "l&rsquo;inventaire, les noms de foyer, les adresses e-mail, les noms d&rsquo;articles ni "
                            "les codes-barres à Analytics. La collecte analytique est désactivée dans les versions de "
                            "débogage et lorsque vous utilisez l&rsquo;application sans compte cloud.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Services tiers",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Google Firebase</strong> &mdash; authentification, base de données cloud, notifications push, fonctions cloud, rapports de plantage/diagnostic, surveillance des performances et analyses d&rsquo;utilisation (lorsque vous êtes connecté à un compte cloud).",
                            "<strong>Open Food Facts</strong> &mdash; recherches de produits par code-barres. Nous envoyons des numéros de code-barres pour rechercher des informations produit&nbsp;; nous n&rsquo;envoyons pas vos listes d&rsquo;inventaire.",
                        ],
                    },
                ],
            },
            {
                "heading": "Conservation et suppression des données",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Nous conservons vos données tant que votre compte est actif. Sans connexion au cloud, "
                            "vous pouvez exporter les données locales depuis <strong>Réglages</strong>.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Les foyers dont vous êtes propriétaire sont supprimés pour tous les membres, qui en "
                            "sont informés. Si vous appartenez à un autre foyer en tant que membre ou administrateur, "
                            "vous êtes retiré et le propriétaire est informé.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Pour supprimer votre compte cloud et les données associées, suivez les étapes sur "
                            "notre <a href=\"{delete_account_url}\">page de demande de suppression de compte</a>, "
                            "utilisez <strong>Réglages &rarr; Compte &rarr; Supprimer le compte</strong> dans "
                            "l&rsquo;application, ou envoyez un e-mail à <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a> depuis votre adresse "
                            "enregistrée.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Confidentialité des enfants",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Larderia ne s&rsquo;adresse pas aux enfants de moins de 13&nbsp;ans. Nous ne "
                            "collectons pas sciemment d&rsquo;informations personnelles auprès d&rsquo;enfants de "
                            "moins de 13&nbsp;ans.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Modifications",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Nous pouvons mettre à jour cette politique de temps à autre. La date "
                            "&laquo;&nbsp;Dernière mise à jour&nbsp;&raquo; en haut de cette page sera modifiée en "
                            "conséquence.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Contact",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Questions concernant cette politique&nbsp;: <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>"
                        ),
                    },
                ],
            },
        ],
    },
    "ja":     {
        "html_lang": "ja",
        "title": "Larderia プライバシーポリシー",
        "updated": "最終更新日：2026年6月21日",
        "sections": [
            {
                "heading": "概要",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Cairn Studio（「当社」）は、モバイルアプリ Larderia を運営しています。Larderia "
                            "は家庭の食品在庫管理を支援します。アカウントなしでご利用いただけます（データはお使いのデバイスに保存されます）。アカウントを作成すれば、デバイス間でデータを同期し、家庭内で共有できます。</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>お問い合わせ：<a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
            {
                "heading": "収集する情報",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>アカウント情報</strong> &mdash; 登録時のメールアドレスと任意の表示名。",
                            "<strong>在庫データ</strong> &mdash; 入力した品目、数量、保管場所、消費・廃棄の記録、カテゴリ、アレルゲン、栄養の設定。",
                            "<strong>家庭データ</strong> &mdash; 家庭名、住所（入力した場合）、メンバーの役割、管理する扶養家族のプロフィール。",
                            "<strong>カメラ（任意）</strong> &mdash; バーコードスキャンとデバイス上の文字認識（栄養表示ラベル、レシート）のみに使用。画像はデバイス上で処理され、バージョン 1.0 では当社サーバーにアップロードされません。",
                            "<strong>商品画像</strong> &mdash; バーコードをスキャンした際、Open Food Facts の商品サムネイル URL を表示する場合があります。当社サーバーには保存しません。",
                            "<strong>プッシュ通知</strong> &mdash; 有効にしたリマインダー通知を送るためのデバイストークン。",
                            "<strong>健康データ（任意）</strong> &mdash; オプトインした場合、記録した消費の栄養情報が Apple Health または Health Connect に書き込まれることがあります。",
                            "<strong>位置情報（任意）</strong> &mdash; その機能を利用する場合に、家庭の住所設定を支援するためにのみ使用。",
                        ],
                    },
                ],
            },
            {
                "heading": "情報の利用目的",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>当社はこのデータを、在庫管理、家庭内共有、レポート、リマインダー、任意の健康データエクスポートの提供に使用します。個人情報を販売することはありません。</p>",
                    },
                ],
            },
            {
                "heading": "データの保存場所",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>ローカルのみモード</strong> &mdash; データはお使いのデバイスに保存されます。OS により、アプリデータがデバイスのバックアップ（例：iCloud バックアップ、Android Auto Backup）に含まれる場合があります。",
                            "<strong>クラウドアカウント</strong> &mdash; データは Google Firebase（Firestore）のアクセス制御されたデータベースに保存されます。認証は Firebase Auth が処理します。バージョン 1.0 ではユーザー写真を Firebase Cloud Storage にアップロードしません。",
                        ],
                    },
                ],
            },
            {
                "heading": "クラッシュ、診断、パフォーマンス、分析",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>リリースビルドでは <strong>Google Firebase Crashlytics</strong>"
                            "を使用し、クラッシュレポートと限定的な診断イベント（同期やプッシュ登録の失敗など）を収集します。レポートには Firebase アカウント "
                            "ID、アプリのバージョン、デバイスの種類、ロケールが含まれる場合があります。在庫の内容、家庭名、メールアドレス、通知トークンは含みません。Xcode または Android "
                            "Studio からデバッグビルドを実行している間はクラッシュ収集は無効です。</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>また <strong>Google Firebase Performance Monitoring</strong>"
                            "を使用し、アプリの起動時間と選択した操作（同期キューの再生など）の所要時間を測定します。パフォーマンスデータにはデバイスの種類、アプリのバージョン、おおまかな時間指標が含まれる場合があります。在庫の内容や "
                            "Firebase アカウント ID 以外の個人識別子は含みません。デバッグビルドではパフォーマンス収集は無効です。</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>クラウドアカウントにサインインしている場合（ローカルのみモード以外）、リリースビルドでは <strong>Google Firebase "
                            "Analytics</strong> を使用してアプリの利用状況を把握します（例：開いた主要画面、サインイン・登録・サインアウト・アカウント削除のタイミング）。分析には "
                            "Firebase アカウント "
                            "ID、アプリのバージョン、デバイスの種類、ロケール、おおまかな操作イベントが含まれる場合があります。在庫の内容、家庭名、メールアドレス、品目名、バーコード番号は "
                            "Analytics に送信しません。デバッグビルドおよびクラウドアカウントなしでの利用時は分析収集は無効です。</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "第三者サービス",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Google Firebase</strong> &mdash; 認証、クラウドデータベース、プッシュ通知、クラウド関数、クラッシュ／診断レポート、パフォーマンス監視、利用分析（クラウドアカウントにサインインしている場合）。",
                            "<strong>Open Food Facts</strong> &mdash; バーコードによる商品検索。商品情報の検索のためバーコード番号を送信します。在庫リストは送信しません。",
                        ],
                    },
                ],
            },
            {
                "heading": "データの保持と削除",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>アカウントが有効な間、データを保持します。クラウドにサインインしていない場合は、<strong>設定</strong>からローカルデータをエクスポートできます。</p>",
                    },
                    {
                        "type": "p",
                        "html": "<p>あなたが所有する家庭は全メンバー向けに削除され、メンバーに通知されます。他の家庭のメンバーまたは管理者として所属している場合は削除され、所有者に通知されます。</p>",
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>クラウドアカウントと関連データを削除するには、<a href=\"{delete_account_url}\">アカウント削除リクエストページ</a>の手順に従うか、アプリの "
                            "<strong>設定 &rarr; アカウント &rarr; アカウントを削除</strong> を使用するか、登録メールアドレスから <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a> にメールしてください。</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "子どものプライバシー",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>Larderia は 13 歳未満の子どもを対象としていません。13 歳未満の子どもから故意に個人情報を収集することはありません。</p>",
                    },
                ],
            },
            {
                "heading": "変更",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>本ポリシーは随時更新される場合があります。更新時にはページ上部の「最終更新日」が変更されます。</p>",
                    },
                ],
            },
            {
                "heading": "お問い合わせ",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>本ポリシーに関するご質問：<a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>"
                        ),
                    },
                ],
            },
        ],
    },
    "ko":     {
        "html_lang": "ko",
        "title": "Larderia 개인정보 처리방침",
        "updated": "최종 업데이트: 2026년 6월 21일",
        "sections": [
            {
                "heading": "개요",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Cairn Studio(&ldquo;당사&rdquo;, &ldquo;우리&rdquo;)는 Larderia 모바일 앱을 운영합니다. Larderia는 "
                            "가정의 식품 재고 관리를 돕습니다. 계정 없이 앱을 사용할 수 있으며(데이터는 기기에 저장됨), 계정을 만들면 기기 간 동기화 및 가구 내 공유가 "
                            "가능합니다.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>문의: <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
            {
                "heading": "수집하는 정보",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>계정 정보</strong> &mdash; 가입 시 이메일 주소 및 선택적 표시 이름.",
                            "<strong>재고 데이터</strong> &mdash; 입력한 품목, 수량, 보관 위치, 소비 및 폐기 기록, 카테고리, 알레르겐, 영양 설정.",
                            "<strong>가구 데이터</strong> &mdash; 가구 이름, 주소(제공한 경우), 구성원 역할, 관리하는 피부양자 프로필.",
                            "<strong>카메라(선택)</strong> &mdash; 바코드 스캔 및 기기 내 문자 인식(영양 성분표, 영수증)에만 사용. 이미지는 기기에서 처리되며 버전 1.0에서는 당사 서버에 업로드되지 않습니다.",
                            "<strong>제품 이미지</strong> &mdash; 바코드를 스캔할 때 Open Food Facts의 제품 썸네일 URL을 표시할 수 있으며, 당사 서버에는 해당 이미지를 저장하지 않습니다.",
                            "<strong>푸시 알림</strong> &mdash; 활성화한 알림을 보내기 위한 기기 토큰.",
                            "<strong>건강 데이터(선택)</strong> &mdash; 동의한 경우 기록된 소비의 영양 정보가 Apple Health 또는 Health Connect에 기록될 수 있습니다.",
                            "<strong>위치(선택)</strong> &mdash; 해당 기능을 사용할 때 가구 주소 설정을 돕기 위해서만 사용.",
                        ],
                    },
                ],
            },
            {
                "heading": "정보 이용 목적",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>당사는 이 데이터를 재고 추적, 가구 공유, 보고서, 알림 및 선택적 건강 데이터보내기 제공에 사용합니다. 개인정보를 판매하지 않습니다.</p>",
                    },
                ],
            },
            {
                "heading": "데이터 저장 위치",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>로컬 전용 모드</strong> &mdash; 데이터는 기기에 저장됩니다. 운영체제에 따라 앱 데이터가 기기 백업(예: iCloud 백업, Android Auto Backup)에 포함될 수 있습니다.",
                            "<strong>클라우드 계정</strong> &mdash; 데이터는 Google Firebase(Firestore)의 접근 제어 데이터베이스에 저장됩니다. 인증은 Firebase Auth가 처리합니다. 버전 1.0에서는 사용자 사진을 Firebase Cloud Storage에 업로드하지 않습니다.",
                        ],
                    },
                ],
            },
            {
                "heading": "충돌, 진단, 성능 및 분석",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>릴리스 빌드에서는 <strong>Google Firebase Crashlytics</strong>를 사용해 충돌 보고서와 제한된 진단 이벤트(동기화 또는 "
                            "푸시 등록 실패 등)를 수집합니다. 보고서에는 Firebase 계정 ID, 앱 버전, 기기 유형, 로케일이 포함될 수 있습니다. 재고 내용, 가구 이름, "
                            "이메일 주소, 알림 토큰은 포함하지 않습니다. Xcode 또는 Android Studio에서 디버그 빌드를 실행하는 동안에는 충돌 수집이 "
                            "비활성화됩니다.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>또한 <strong>Google Firebase Performance Monitoring</strong>으로 앱 시작 시간과 선택한 작업(동기화 대기열 "
                            "재생 등) 소요 시간을 측정합니다. 성능 데이터에는 기기 유형, 앱 버전, 대략적인 시간 지표가 포함될 수 있습니다. 재고 내용이나 Firebase 계정 ID "
                            "이외의 개인 식별 정보는 포함하지 않습니다. 디버그 빌드에서는 성능 수집이 비활성화됩니다.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>클라우드 계정에 로그인한 경우(로컬 전용 모드가 아닌 경우) 릴리스 빌드에서 <strong>Google Firebase "
                            "Analytics</strong>를 사용해 앱 이용 방식을 파악합니다(예: 열어본 주요 화면, 로그인·가입·로그아웃·계정 삭제 시점). 분석에는 "
                            "Firebase 계정 ID, 앱 버전, 기기 유형, 로케일, 대략적인 상호작용 이벤트가 포함될 수 있습니다. 재고 내용, 가구 이름, 이메일 주소, 품목 "
                            "이름, 바코드 번호는 Analytics로 보내지 않습니다. 디버그 빌드 및 클라우드 계정 없이 사용할 때는 분석 수집이 비활성화됩니다.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "제3자 서비스",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Google Firebase</strong> &mdash; 인증, 클라우드 데이터베이스, 푸시 알림, 클라우드 함수, 충돌/진단 보고, 성능 모니터링, 이용 분석(클라우드 계정 로그인 시).",
                            "<strong>Open Food Facts</strong> &mdash; 바코드 제품 조회. 제품 정보 조회를 위해 바코드 번호를 전송하며, 재고 목록은 전송하지 않습니다.",
                        ],
                    },
                ],
            },
            {
                "heading": "데이터 보관 및 삭제",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>계정이 활성인 동안 데이터를 보관합니다. 클라우드에 로그인하지 않은 경우 <strong>설정</strong>에서 로컬 데이터를보낼 수 있습니다.</p>",
                    },
                    {
                        "type": "p",
                        "html": "<p>소유한 가구는 모든 구성원에 대해 삭제되며 구성원에게 알립니다. 다른 가구의 구성원 또는 관리자인 경우 제거되며 소유자에게 알립니다.</p>",
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>클라우드 계정 및 관련 데이터를 삭제하려면 <a href=\"{delete_account_url}\">계정 삭제 요청 페이지</a>의 안내를 따르거나, "
                            "앱에서 <strong>설정 &rarr; 계정 &rarr; 계정 삭제</strong>를 사용하거나, 등록된 이메일 주소로 <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a>에 문의하세요.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "아동 개인정보",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>Larderia는 13세 미만 아동을 대상으로 하지 않습니다. 13세 미만 아동의 개인정보를 고의로 수집하지 않습니다.</p>",
                    },
                ],
            },
            {
                "heading": "변경",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>본 방침은 수시로 업데이트될 수 있습니다. 업데이트 시 이 페이지 상단의 &ldquo;최종 업데이트&rdquo; 날짜가 변경됩니다.</p>",
                    },
                ],
            },
            {
                "heading": "문의",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>본 방침 관련 문의: <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>"
                        ),
                    },
                ],
            },
        ],
    },
    "pt":     {
        "html_lang": "pt",
        "title": "Política de Privacidade do Larderia",
        "updated": "Última atualização: 21 de junho de 2026",
        "sections": [
            {
                "heading": "Visão geral",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>A Cairn Studio (&ldquo;nós&rdquo;, &ldquo;nos&rdquo;) opera o aplicativo móvel "
                            "Larderia. O Larderia ajuda os lares a controlar o inventário de alimentos. Você pode "
                            "usar o app sem conta (os dados permanecem no seu dispositivo) ou criar uma conta para "
                            "sincronizar dados entre dispositivos e compartilhar com um lar.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>Contato: <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
            {
                "heading": "Informações que coletamos",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Informações da conta</strong> &mdash; endereço de e-mail e nome de exibição opcional ao se cadastrar.",
                            "<strong>Dados de inventário</strong> &mdash; itens, quantidades, locais de armazenamento, registros de consumo e desperdício, categorias, alérgenos e preferências nutricionais que você inserir.",
                            "<strong>Dados do lar</strong> &mdash; nome do lar, endereço (se fornecido), funções dos membros e perfis de dependentes gerenciados.",
                            "<strong>Câmera (opcional)</strong> &mdash; usada apenas para leitura de códigos de barras e reconhecimento de texto no dispositivo (rótulos nutricionais, recibos). As imagens são processadas no seu dispositivo e não são enviadas aos nossos servidores na versão 1.0.",
                            "<strong>Imagens de produtos</strong> &mdash; ao escanear um código de barras, podemos exibir uma miniatura do produto do Open Food Facts; não armazenamos essa imagem em nossos servidores.",
                            "<strong>Notificações push</strong> &mdash; tokens do dispositivo para enviar lembretes que você ativar.",
                            "<strong>Dados de saúde (opcional)</strong> &mdash; se você optar por participar, informações nutricionais do consumo registrado podem ser gravadas no Apple Health ou Health Connect no seu dispositivo.",
                            "<strong>Localização (opcional)</strong> &mdash; usada apenas para ajudar a definir o endereço do seu lar quando você escolher usar esse recurso.",
                        ],
                    },
                ],
            },
            {
                "heading": "Como usamos as informações",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Usamos esses dados para fornecer controle de inventário, compartilhamento no lar, "
                            "relatórios, lembretes e exportação opcional de dados de saúde. Não vendemos suas "
                            "informações pessoais.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Onde os dados são armazenados",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Modo somente local</strong> &mdash; os dados ficam no seu dispositivo. O sistema operacional pode incluir os dados do app em backups do dispositivo (por exemplo, backup do iCloud ou Android Auto Backup).",
                            "<strong>Contas na nuvem</strong> &mdash; os dados são armazenados no Google Firebase (Firestore) em bancos de dados com controle de acesso. A autenticação é feita pelo Firebase Auth. A versão 1.0 não envia fotos do usuário ao Firebase Cloud Storage.",
                        ],
                    },
                ],
            },
            {
                "heading": "Falhas, diagnóstico, desempenho e análises",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Em builds de lançamento, usamos o <strong>Google Firebase Crashlytics</strong> para "
                            "coletar relatórios de falhas e eventos de diagnóstico limitados (por exemplo, falhas de "
                            "sincronização ou registro push). Os relatórios podem incluir seu ID de conta Firebase, "
                            "versão do app, tipo de dispositivo e localidade. Não incluímos conteúdo do inventário, "
                            "nomes de lares, endereços de e-mail ou tokens de notificação. A coleta de falhas é "
                            "desativada ao executar um build de depuração do Xcode ou Android Studio.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Também usamos o <strong>Google Firebase Performance Monitoring</strong> para medir o "
                            "tempo de inicialização do app e a duração de operações selecionadas (por exemplo, "
                            "reprodução da fila de sincronização). Os dados de desempenho podem incluir tipo de "
                            "dispositivo, versão do app e métricas de tempo aproximadas. Não incluem conteúdo do "
                            "inventário nem identificadores pessoais além do seu ID de conta Firebase. A coleta de "
                            "desempenho é desativada em builds de depuração.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Quando você está conectado a uma conta na nuvem (não no modo somente local), usamos o "
                            "<strong>Google Firebase Analytics</strong> em builds de lançamento para entender como o "
                            "app é usado &mdash; por exemplo, quais telas principais você abre e quando faz login, "
                            "cadastro, logout ou exclui sua conta. As análises podem incluir seu ID de conta "
                            "Firebase, versão do app, tipo de dispositivo, localidade e eventos de interação gerais. "
                            "Não enviamos conteúdo do inventário, nomes de lares, e-mails, nomes de itens ou códigos "
                            "de barras ao Analytics. A coleta analítica é desativada em builds de depuração e quando "
                            "você usa o app sem conta na nuvem.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Serviços de terceiros",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Google Firebase</strong> &mdash; autenticação, banco de dados na nuvem, notificações push, funções na nuvem, relatórios de falha/diagnóstico, monitoramento de desempenho e análises de uso (quando conectado a uma conta na nuvem).",
                            "<strong>Open Food Facts</strong> &mdash; consultas de produtos por código de barras. Enviamos números de código de barras para buscar informações do produto; não enviamos suas listas de inventário.",
                        ],
                    },
                ],
            },
            {
                "heading": "Retenção e exclusão de dados",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Retemos seus dados enquanto sua conta estiver ativa. Sem login na nuvem, você pode "
                            "exportar dados locais em <strong>Configurações</strong>.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Os lares que você possui são excluídos para todos os membros, que são notificados. Se "
                            "você pertence a outro lar como membro ou administrador, é removido e o proprietário é "
                            "notificado.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Para excluir sua conta na nuvem e os dados associados, siga as etapas em nossa <a "
                            "href=\"{delete_account_url}\">página de solicitação de exclusão de conta</a>, use "
                            "<strong>Configurações &rarr; Conta &rarr; Excluir conta</strong> no app ou envie um "
                            "e-mail para <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a> do "
                            "seu endereço registrado.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Privacidade de crianças",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>O Larderia não é destinado a crianças menores de 13 anos. Não coletamos "
                            "intencionalmente informações pessoais de crianças menores de 13 anos.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Alterações",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Podemos atualizar esta política periodicamente. A data &ldquo;Última "
                            "atualização&rdquo; no topo desta página será alterada quando isso ocorrer.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Contato",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Dúvidas sobre esta política: <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>"
                        ),
                    },
                ],
            },
        ],
    },
    "zh":     {
        "html_lang": "zh",
        "title": "Larderia 隐私政策",
        "updated": "最后更新：2026年6月21日",
        "sections": [
            {
                "heading": "概述",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Cairn Studio（「我们」）运营 Larderia 移动应用。Larderia "
                            "帮助家庭管理食品库存。您可以在不注册账户的情况下使用应用（数据保留在您的设备上），也可以创建账户以在设备间同步数据并与家庭成员共享。</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>联系方式：<a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
            {
                "heading": "我们收集的信息",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>账户信息</strong> &mdash; 注册时的电子邮件地址和可选的显示名称。",
                            "<strong>库存数据</strong> &mdash; 您输入的物品、数量、存放位置、消费与浪费记录、分类、过敏原及营养偏好。",
                            "<strong>家庭数据</strong> &mdash; 家庭名称、地址（如您提供）、成员角色及受管理的被抚养人资料。",
                            "<strong>相机（可选）</strong> &mdash; 仅用于条形码扫描及设备端文字识别（营养标签、收据）。图像在您的设备上处理，在 1.0 版本中不会上传至我们的服务器。",
                            "<strong>商品图片</strong> &mdash; 扫描条形码时，我们可能显示来自 Open Food Facts 的商品缩略图 URL；我们不会将该图片存储在服务器上。",
                            "<strong>推送通知</strong> &mdash; 设备令牌，用于发送您启用的提醒通知。",
                            "<strong>健康数据（可选）</strong> &mdash; 如您选择加入，已记录消费的营养信息可能会写入您设备上的 Apple Health 或 Health Connect。",
                            "<strong>位置（可选）</strong> &mdash; 仅在您选择使用该功能时，用于帮助设置家庭地址。",
                        ],
                    },
                ],
            },
            {
                "heading": "我们如何使用信息",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>我们使用这些数据提供库存跟踪、家庭共享、报告、提醒及可选的健康数据导出。我们不会出售您的个人信息。</p>",
                    },
                ],
            },
            {
                "heading": "数据存储位置",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>仅本地模式</strong> &mdash; 数据存储在您的设备上。操作系统可能会将应用数据纳入设备备份（例如 iCloud 备份或 Android 自动备份）。",
                            "<strong>云账户</strong> &mdash; 数据存储在 Google Firebase（Firestore）的访问控制数据库中。身份验证由 Firebase Auth 处理。1.0 版本不会将用户照片上传至 Firebase Cloud Storage。",
                        ],
                    },
                ],
            },
            {
                "heading": "崩溃、诊断、性能与分析",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>在发布版本中，我们使用 <strong>Google Firebase Crashlytics</strong>"
                            "收集崩溃报告及有限的诊断事件（例如同步或推送注册失败）。报告可能包含您的 Firebase 账户 "
                            "ID、应用版本、设备类型和语言区域。报告中不包含库存内容、家庭名称、电子邮件地址或通知令牌。在通过 Xcode 或 Android Studio "
                            "运行调试版本时，崩溃收集会被禁用。</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>我们还使用 <strong>Google Firebase Performance Monitoring</strong>"
                            "测量应用启动时间及选定操作的耗时（例如同步队列重放）。性能数据可能包含设备类型、应用版本及粗略的时间指标。其中不包含库存内容或除 Firebase 账户 ID "
                            "以外的个人标识符。调试版本中性能收集会被禁用。</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>当您登录云账户（非仅本地模式）时，我们在发布版本中使用 <strong>Google Firebase Analytics</strong> 了解应用的使用情况 "
                            "&mdash; 例如您打开的主要界面，以及登录、注册、退出或删除账户的时间。分析数据可能包含 Firebase 账户 "
                            "ID、应用版本、设备类型、语言区域及粗略的交互事件。我们不会将库存内容、家庭名称、电子邮件地址、物品名称或条形码发送至 "
                            "Analytics。在调试版本及未使用云账户时，分析收集会被禁用。</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "第三方服务",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Google Firebase</strong> &mdash; 身份验证、云数据库、推送通知、云函数、崩溃/诊断报告、性能监控及使用分析（登录云账户时）。",
                            "<strong>Open Food Facts</strong> &mdash; 条形码商品查询。我们发送条形码号码以查询商品信息；不会发送您的库存清单。",
                        ],
                    },
                ],
            },
            {
                "heading": "数据保留与删除",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>在您的账户处于活跃状态期间，我们会保留您的数据。未登录云账户时，您可以从<strong>设置</strong>导出本地数据。</p>",
                    },
                    {
                        "type": "p",
                        "html": "<p>您拥有的家庭将对所有成员删除，并会通知成员。若您作为成员或管理员属于其他家庭，您将被移除，且会通知该家庭的所有者。</p>",
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>要删除您的云账户及相关数据，请按照<a href=\"{delete_account_url}\">账户删除申请页面</a>的步骤操作，在应用中使用<strong>设置 "
                            "&rarr; 账户 &rarr; 删除账户</strong>，或从您注册的电子邮件地址发送邮件至 <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a>。</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "儿童隐私",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>Larderia 不面向 13 岁以下儿童。我们不会故意收集 13 岁以下儿童的个人信息。</p>",
                    },
                ],
            },
            {
                "heading": "变更",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>我们可能会不时更新本政策。更新时，本页顶部的「最后更新」日期将会变更。</p>",
                    },
                ],
            },
            {
                "heading": "联系我们",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>有关本政策的问题：<a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
        ],
    },
    "zh-Hant":     {
        "html_lang": "zh-Hant",
        "title": "Larderia 隱私權政策",
        "updated": "最後更新：2026年6月21日",
        "sections": [
            {
                "heading": "概述",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Cairn Studio（「我們」）營運 Larderia 行動應用程式。Larderia "
                            "協助家庭管理食品庫存。您可以在不註冊帳戶的情況下使用應用程式（資料保留在您的裝置上），也可以建立帳戶以在裝置間同步資料並與家庭成員共享。</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>聯絡方式：<a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
            {
                "heading": "我們收集的資訊",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>帳戶資訊</strong> &mdash; 註冊時的電子郵件地址和選用的顯示名稱。",
                            "<strong>庫存資料</strong> &mdash; 您輸入的物品、數量、存放位置、消費與浪費記錄、分類、過敏原及營養偏好。",
                            "<strong>家庭資料</strong> &mdash; 家庭名稱、地址（若您提供）、成員角色及受管理的被撫養人資料。",
                            "<strong>相機（選用）</strong> &mdash; 僅用於條碼掃描及裝置端文字辨識（營養標籤、收據）。影像在您的裝置上處理，在 1.0 版本中不會上傳至我們的伺服器。",
                            "<strong>商品圖片</strong> &mdash; 掃描條碼時，我們可能顯示來自 Open Food Facts 的商品縮圖 URL；我們不會將該圖片儲存在伺服器上。",
                            "<strong>推播通知</strong> &mdash; 裝置權杖，用於傳送您啟用的提醒通知。",
                            "<strong>健康資料（選用）</strong> &mdash; 若您選擇加入，已記錄消費的營養資訊可能會寫入您裝置上的 Apple Health 或 Health Connect。",
                            "<strong>位置（選用）</strong> &mdash; 僅在您選擇使用該功能時，用於協助設定家庭地址。",
                        ],
                    },
                ],
            },
            {
                "heading": "我們如何使用資訊",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>我們使用這些資料提供庫存追蹤、家庭共享、報告、提醒及選用的健康資料匯出。我們不會出售您的個人資訊。</p>",
                    },
                ],
            },
            {
                "heading": "資料儲存位置",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>僅本機模式</strong> &mdash; 資料儲存在您的裝置上。作業系統可能會將應用程式資料納入裝置備份（例如 iCloud 備份或 Android 自動備份）。",
                            "<strong>雲端帳戶</strong> &mdash; 資料儲存在 Google Firebase（Firestore）的存取控制資料庫中。身分驗證由 Firebase Auth 處理。1.0 版本不會將使用者照片上傳至 Firebase Cloud Storage。",
                        ],
                    },
                ],
            },
            {
                "heading": "當機、診斷、效能與分析",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>在正式版本中，我們使用 <strong>Google Firebase Crashlytics</strong>"
                            "收集當機報告及有限的診斷事件（例如同步或推播註冊失敗）。報告可能包含您的 Firebase 帳戶 "
                            "ID、應用程式版本、裝置類型及語言地區。報告中不包含庫存內容、家庭名稱、電子郵件地址或通知權杖。透過 Xcode 或 Android Studio "
                            "執行偵錯版本時，當機收集會停用。</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>我們也使用 <strong>Google Firebase Performance Monitoring</strong>"
                            "測量應用程式啟動時間及選定作業的耗時（例如同步佇列重放）。效能資料可能包含裝置類型、應用程式版本及粗略的時間指標。其中不包含庫存內容或除 Firebase 帳戶 ID "
                            "以外的個人識別資訊。偵錯版本中效能收集會停用。</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>當您登入雲端帳戶（非僅本機模式）時，我們在正式版本中使用 <strong>Google Firebase Analytics</strong> 了解應用程式的使用情況 "
                            "&mdash; 例如您開啟的主要畫面，以及登入、註冊、登出或刪除帳戶的時間。分析資料可能包含 Firebase 帳戶 "
                            "ID、應用程式版本、裝置類型、語言地區及粗略的互動事件。我們不會將庫存內容、家庭名稱、電子郵件地址、物品名稱或條碼傳送至 "
                            "Analytics。在偵錯版本及未使用雲端帳戶時，分析收集會停用。</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "第三方服務",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "<strong>Google Firebase</strong> &mdash; 身分驗證、雲端資料庫、推播通知、雲端函式、當機/診斷報告、效能監控及使用分析（登入雲端帳戶時）。",
                            "<strong>Open Food Facts</strong> &mdash; 條碼商品查詢。我們傳送條碼號碼以查詢商品資訊；不會傳送您的庫存清單。",
                        ],
                    },
                ],
            },
            {
                "heading": "資料保留與刪除",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>在您的帳戶處於使用中期間，我們會保留您的資料。未登入雲端帳戶時，您可以從<strong>設定</strong>匯出本機資料。</p>",
                    },
                    {
                        "type": "p",
                        "html": "<p>您擁有的家庭將對所有成員刪除，並會通知成員。若您作為成員或管理員屬於其他家庭，您將被移除，且會通知該家庭的所有者。</p>",
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>若要刪除您的雲端帳戶及相關資料，請依照<a "
                            "href=\"{delete_account_url}\">帳戶刪除申請頁面</a>的步驟操作，在應用程式中使用<strong>設定 &rarr; 帳戶 &rarr; "
                            "刪除帳戶</strong>，或從您註冊的電子郵件地址寄信至 <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a>。</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "兒童隱私",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>Larderia 不面向 13 歲以下兒童。我們不會故意收集 13 歲以下兒童的個人資訊。</p>",
                    },
                ],
            },
            {
                "heading": "變更",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>我們可能會不時更新本政策。更新時，本頁頂部的「最後更新」日期將會變更。</p>",
                    },
                ],
            },
            {
                "heading": "聯絡我們",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>有關本政策的問題：<a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
        ],
    },
}

DELETE_ACCOUNT_PAGES = {
    "en":     {
        "html_lang": "en",
        "title": "Request account deletion",
        "updated": "Last updated: June 21, 2026",
        "sections": [
            {
                "heading": "Delete in the app (recommended)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>If you are signed in to a cloud account, you can permanently delete your account and "
                            "associated cloud data from the app:</p>"
                        ),
                    },
                    {
                        "type": "ol",
                        "items": [
                            "Open <strong>Settings</strong>",
                            "Tap your profile, then open <strong>Account</strong>",
                            "Tap <strong>Delete account</strong> and confirm with your password",
                        ],
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Deletion is immediate. You will be signed out and local app data on that device is "
                            "cleared.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Request deletion by email",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>If you cannot access the app, email us from the address registered to your Larderia "
                            "account. We will verify ownership and delete your account and cloud data.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p><a class=\"cta\""
                            "href=\"mailto:support@cairn-studio.com?subject=Larderia%20account%20deletion%20request\">Email "
                            "support@cairn-studio.com</a></p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Include your registered email address in the message. We may ask you to confirm the "
                            "request before processing it.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "What is deleted",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "Your Firebase Auth account and user profile",
                            "Households you own, including inventory and locations stored in our cloud",
                            "Your membership in households owned by others (the owner is notified)",
                            "Push notification tokens associated with your account",
                        ],
                    },
                ],
            },
            {
                "heading": "Local-only use (no cloud account)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>If you use Larderia without an account, your data is stored only on your device. "
                            "Uninstalling the app or clearing app storage removes that data. You can also export a "
                            "backup from <strong>Settings</strong> before doing so.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "More information",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>See our <a href=\"{privacy_url}\">Privacy Policy</a> for how we collect and use "
                            "data.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>Questions: <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
        ],
    },
    "de":     {
        "html_lang": "de",
        "title": "Kontolöschung beantragen",
        "updated": "Zuletzt aktualisiert: 21. Juni 2026",
        "sections": [
            {
                "heading": "In der App löschen (empfohlen)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Wenn Sie bei einem Cloud-Konto angemeldet sind, können Sie Ihr Konto und zugehörige "
                            "Cloud-Daten dauerhaft in der App löschen:</p>"
                        ),
                    },
                    {
                        "type": "ol",
                        "items": [
                            "Öffnen Sie <strong>Einstellungen</strong>",
                            "Tippen Sie auf Ihr Profil und öffnen Sie <strong>Konto</strong>",
                            "Tippen Sie auf <strong>Konto löschen</strong> und bestätigen Sie mit Ihrem Passwort",
                        ],
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Die Löschung erfolgt sofort. Sie werden abgemeldet und lokale App-Daten auf diesem "
                            "Gerät werden gelöscht.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Löschung per E-Mail beantragen",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Wenn Sie keinen Zugriff auf die App haben, senden Sie uns eine E-Mail von der mit "
                            "Ihrem Larderia-Konto registrierten Adresse. Wir prüfen die Inhaberschaft und löschen Ihr "
                            "Konto und Cloud-Daten.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p><a class=\"cta\""
                            "href=\"mailto:support@cairn-studio.com?subject=Larderia%20account%20deletion%20request\">E-Mail "
                            "an support@cairn-studio.com</a></p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Geben Sie Ihre registrierte E-Mail-Adresse in der Nachricht an. Wir können Sie "
                            "bitten, die Anfrage vor der Bearbeitung zu bestätigen.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Was gelöscht wird",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "Ihr Firebase-Auth-Konto und Benutzerprofil",
                            "Haushalte, die Ihnen gehören, einschließlich Bestand und Standorte in unserer Cloud",
                            "Ihre Mitgliedschaft in Haushalten anderer Eigentümer (der Eigentümer wird benachrichtigt)",
                            "Mit Ihrem Konto verknüpfte Push-Benachrichtigungstoken",
                        ],
                    },
                ],
            },
            {
                "heading": "Nur-lokale Nutzung (ohne Cloud-Konto)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Wenn Sie Larderia ohne Konto nutzen, werden Ihre Daten nur auf Ihrem Gerät "
                            "gespeichert. Deinstallation der App oder Löschen des App-Speichers entfernt diese Daten. "
                            "Sie können vorher auch ein Backup unter <strong>Einstellungen</strong> exportieren.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Weitere Informationen",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Informationen zur Erhebung und Nutzung von Daten finden Sie in unserer <a "
                            "href=\"{privacy_url}\">Datenschutzerklärung</a>.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>Fragen: <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
        ],
    },
    "es":     {
        "html_lang": "es",
        "title": "Solicitar eliminación de cuenta",
        "updated": "Última actualización: 21 de junio de 2026",
        "sections": [
            {
                "heading": "Eliminar en la app (recomendado)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Si ha iniciado sesión en una cuenta en la nube, puede eliminar permanentemente su "
                            "cuenta y los datos asociados en la nube desde la app:</p>"
                        ),
                    },
                    {
                        "type": "ol",
                        "items": [
                            "Abra <strong>Ajustes</strong>",
                            "Toque su perfil y abra <strong>Cuenta</strong>",
                            "Toque <strong>Eliminar cuenta</strong> y confirme con su contraseña",
                        ],
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>La eliminación es inmediata. Se cerrará su sesión y se borrarán los datos locales de "
                            "la app en ese dispositivo.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Solicitar eliminación por correo",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Si no puede acceder a la app, envíenos un correo desde la dirección registrada en su "
                            "cuenta de Larderia. Verificaremos la titularidad y eliminaremos su cuenta y datos en la "
                            "nube.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p><a class=\"cta\""
                            "href=\"mailto:support@cairn-studio.com?subject=Larderia%20account%20deletion%20request\">Enviar "
                            "correo a support@cairn-studio.com</a></p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Incluya su dirección de correo registrada en el mensaje. Podemos pedirle que confirme "
                            "la solicitud antes de procesarla.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Qué se elimina",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "Su cuenta de Firebase Auth y perfil de usuario",
                            "Hogares de su propiedad, incluido inventario y ubicaciones almacenados en nuestra nube",
                            "Su pertenencia a hogares de otros propietarios (el propietario es notificado)",
                            "Tokens de notificaciones push asociados a su cuenta",
                        ],
                    },
                ],
            },
            {
                "heading": "Uso solo local (sin cuenta en la nube)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Si usa Larderia sin cuenta, sus datos se almacenan solo en su dispositivo. "
                            "Desinstalar la app o borrar el almacenamiento de la app elimina esos datos. También "
                            "puede exportar una copia de seguridad desde <strong>Ajustes</strong> antes de "
                            "hacerlo.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Más información",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Consulte nuestra <a href=\"{privacy_url}\">Política de privacidad</a> para saber cómo "
                            "recopilamos y usamos los datos.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>Preguntas: <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
        ],
    },
    "fr":     {
        "html_lang": "fr",
        "title": "Demander la suppression du compte",
        "updated": "Dernière mise à jour : 21 juin 2026",
        "sections": [
            {
                "heading": "Supprimer dans l&rsquo;application (recommandé)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Si vous êtes connecté à un compte cloud, vous pouvez supprimer définitivement votre "
                            "compte et les données cloud associées depuis l&rsquo;application&nbsp;:</p>"
                        ),
                    },
                    {
                        "type": "ol",
                        "items": [
                            "Ouvrez <strong>Réglages</strong>",
                            "Appuyez sur votre profil, puis ouvrez <strong>Compte</strong>",
                            "Appuyez sur <strong>Supprimer le compte</strong> et confirmez avec votre mot de passe",
                        ],
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>La suppression est immédiate. Vous serez déconnecté et les données locales de "
                            "l&rsquo;application sur cet appareil seront effacées.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Demander la suppression par e-mail",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Si vous ne pouvez pas accéder à l&rsquo;application, envoyez-nous un e-mail depuis "
                            "l&rsquo;adresse enregistrée sur votre compte Larderia. Nous vérifierons la propriété et "
                            "supprimerons votre compte et vos données cloud.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p><a class=\"cta\""
                            "href=\"mailto:support@cairn-studio.com?subject=Larderia%20account%20deletion%20request\">Envoyer "
                            "un e-mail à support@cairn-studio.com</a></p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Incluez votre adresse e-mail enregistrée dans le message. Nous pouvons vous demander "
                            "de confirmer la demande avant de la traiter.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Ce qui est supprimé",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "Votre compte Firebase Auth et profil utilisateur",
                            "Les foyers dont vous êtes propriétaire, y compris l&rsquo;inventaire et les emplacements stockés dans notre cloud",
                            "Votre appartenance à des foyers appartenant à d&rsquo;autres personnes (le propriétaire est informé)",
                            "Les jetons de notifications push associés à votre compte",
                        ],
                    },
                ],
            },
            {
                "heading": "Utilisation locale uniquement (sans compte cloud)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Si vous utilisez Larderia sans compte, vos données sont stockées uniquement sur votre "
                            "appareil. Désinstaller l&rsquo;application ou effacer son stockage supprime ces données. "
                            "Vous pouvez aussi exporter une sauvegarde depuis <strong>Réglages</strong> avant de le "
                            "faire.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Plus d&rsquo;informations",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Consultez notre <a href=\"{privacy_url}\">Politique de confidentialité</a> pour savoir "
                            "comment nous collectons et utilisons les données.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Questions&nbsp;: <a "
                            "href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>"
                        ),
                    },
                ],
            },
        ],
    },
    "ja":     {
        "html_lang": "ja",
        "title": "アカウント削除の申請",
        "updated": "最終更新日：2026年6月21日",
        "sections": [
            {
                "heading": "アプリ内で削除（推奨）",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>クラウドアカウントにサインインしている場合、アプリからアカウントと関連するクラウドデータを完全に削除できます：</p>",
                    },
                    {
                        "type": "ol",
                        "items": [
                            "<strong>設定</strong>を開く",
                            "プロフィールをタップし、<strong>アカウント</strong>を開く",
                            "<strong>アカウントを削除</strong>をタップし、パスワードで確認する",
                        ],
                    },
                    {
                        "type": "p",
                        "html": "<p>削除は即時に行われます。サインアウトされ、そのデバイスのローカルアプリデータは消去されます。</p>",
                    },
                ],
            },
            {
                "heading": "メールで削除を申請",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>アプリにアクセスできない場合、Larderia "
                            "アカウントに登録されたアドレスからメールでご連絡ください。所有者を確認のうえ、アカウントとクラウドデータを削除します。</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p><a class=\"cta\""
                            "href=\"mailto:support@cairn-studio.com?subject=Larderia%20account%20deletion%20request\">support@cairn-studio.com "
                            "にメール</a></p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>メッセージに登録メールアドレスを記載してください。処理前に申請の確認をお願いする場合があります。</p>",
                    },
                ],
            },
            {
                "heading": "削除される内容",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "Firebase Auth アカウントとユーザープロフィール",
                            "あなたが所有する家庭（クラウドに保存された在庫と保管場所を含む）",
                            "他の所有者の家庭への所属（所有者に通知されます）",
                            "アカウントに関連付けられたプッシュ通知トークン",
                        ],
                    },
                ],
            },
            {
                "heading": "ローカルのみの利用（クラウドアカウントなし）",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>アカウントなしで Larderia "
                            "を使用している場合、データはデバイスにのみ保存されます。アプリをアンインストールするか、アプリのストレージを消去するとデータは削除されます。事前に<strong>設定</strong>からバックアップをエクスポートすることもできます。</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "詳細情報",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>データの収集と利用については<a href=\"{privacy_url}\">プライバシーポリシー</a>をご覧ください。</p>",
                    },
                    {
                        "type": "p",
                        "html": "<p>お問い合わせ：<a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
        ],
    },
    "ko":     {
        "html_lang": "ko",
        "title": "계정 삭제 요청",
        "updated": "최종 업데이트: 2026년 6월 21일",
        "sections": [
            {
                "heading": "앱에서 삭제(권장)",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>클라우드 계정에 로그인한 경우 앱에서 계정 및 관련 클라우드 데이터를 영구적으로 삭제할 수 있습니다:</p>",
                    },
                    {
                        "type": "ol",
                        "items": [
                            "<strong>설정</strong> 열기",
                            "프로필을 탭한 후 <strong>계정</strong> 열기",
                            "<strong>계정 삭제</strong>를 탭하고 비밀번호로 확인",
                        ],
                    },
                    {
                        "type": "p",
                        "html": "<p>삭제는 즉시 이루어집니다. 로그아웃되며 해당 기기의 로컬 앱 데이터가 삭제됩니다.</p>",
                    },
                ],
            },
            {
                "heading": "이메일로 삭제 요청",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>앱에 접근할 수 없는 경우 Larderia 계정에 등록된 주소로 이메일을 보내 주세요. 소유권을 확인한 후 계정과 클라우드 데이터를 삭제합니다.</p>",
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p><a class=\"cta\""
                            "href=\"mailto:support@cairn-studio.com?subject=Larderia%20account%20deletion%20request\">support@cairn-studio.com "
                            "으로 이메일</a></p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>메시지에 등록된 이메일 주소를 포함해 주세요. 처리 전 요청 확인을 요청할 수 있습니다.</p>",
                    },
                ],
            },
            {
                "heading": "삭제되는 항목",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "Firebase Auth 계정 및 사용자 프로필",
                            "소유한 가구(클라우드에 저장된 재고 및 위치 포함)",
                            "다른 소유자의 가구 구성원 자격(소유자에게 알림)",
                            "계정과 연결된 푸시 알림 토큰",
                        ],
                    },
                ],
            },
            {
                "heading": "로컬 전용 사용(클라우드 계정 없음)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>계정 없이 Larderia를 사용하는 경우 데이터는 기기에만 저장됩니다. 앱을 제거하거나 앱 저장소를 지우면 해당 데이터가 삭제됩니다. 그 전에 "
                            "<strong>설정</strong>에서 백업을보낼 수도 있습니다.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "추가 정보",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>데이터 수집 및 이용 방법은 <a href=\"{privacy_url}\">개인정보 처리방침</a>을 참고하세요.</p>",
                    },
                    {
                        "type": "p",
                        "html": "<p>문의: <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
        ],
    },
    "pt":     {
        "html_lang": "pt",
        "title": "Solicitar exclusão de conta",
        "updated": "Última atualização: 21 de junho de 2026",
        "sections": [
            {
                "heading": "Excluir no app (recomendado)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Se você estiver conectado a uma conta na nuvem, pode excluir permanentemente sua "
                            "conta e os dados na nuvem associados pelo app:</p>"
                        ),
                    },
                    {
                        "type": "ol",
                        "items": [
                            "Abra <strong>Configurações</strong>",
                            "Toque no seu perfil e abra <strong>Conta</strong>",
                            "Toque em <strong>Excluir conta</strong> e confirme com sua senha",
                        ],
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>A exclusão é imediata. Você será desconectado e os dados locais do app nesse "
                            "dispositivo serão apagados.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Solicitar exclusão por e-mail",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Se não puder acessar o app, envie um e-mail do endereço registrado na sua conta "
                            "Larderia. Verificaremos a titularidade e excluiremos sua conta e dados na nuvem.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p><a class=\"cta\""
                            "href=\"mailto:support@cairn-studio.com?subject=Larderia%20account%20deletion%20request\">Enviar "
                            "e-mail para support@cairn-studio.com</a></p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p>Inclua seu endereço de e-mail registrado na mensagem. Podemos pedir que você confirme "
                            "a solicitação antes de processá-la.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "O que é excluído",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "Sua conta Firebase Auth e perfil de usuário",
                            "Lares que você possui, incluindo inventário e locais armazenados em nossa nuvem",
                            "Sua participação em lares de outros proprietários (o proprietário é notificado)",
                            "Tokens de notificações push associados à sua conta",
                        ],
                    },
                ],
            },
            {
                "heading": "Uso somente local (sem conta na nuvem)",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Se você usa o Larderia sem conta, seus dados ficam apenas no seu dispositivo. "
                            "Desinstalar o app ou limpar o armazenamento do app remove esses dados. Você também pode "
                            "exportar um backup em <strong>Configurações</strong> antes disso.</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "Mais informações",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>Consulte nossa <a href=\"{privacy_url}\">Política de Privacidade</a> para saber como "
                            "coletamos e usamos os dados.</p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>Dúvidas: <a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
        ],
    },
    "zh":     {
        "html_lang": "zh",
        "title": "申请删除账户",
        "updated": "最后更新：2026年6月21日",
        "sections": [
            {
                "heading": "在应用中删除（推荐）",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>如果您已登录云账户，可以在应用中永久删除您的账户及相关的云数据：</p>",
                    },
                    {
                        "type": "ol",
                        "items": [
                            "打开<strong>设置</strong>",
                            "点按您的个人资料，然后打开<strong>账户</strong>",
                            "点按<strong>删除账户</strong>并使用密码确认",
                        ],
                    },
                    {
                        "type": "p",
                        "html": "<p>删除立即生效。您将退出登录，该设备上的本地应用数据将被清除。</p>",
                    },
                ],
            },
            {
                "heading": "通过电子邮件申请删除",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>如果您无法访问应用，请从 Larderia 账户注册的地址向我们发送电子邮件。我们将核实所有权并删除您的账户及云数据。</p>",
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p><a class=\"cta\""
                            "href=\"mailto:support@cairn-studio.com?subject=Larderia%20account%20deletion%20request\">发送邮件至 "
                            "support@cairn-studio.com</a></p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>请在邮件中包含您注册的电子邮件地址。我们可能会在处理前要求您确认该请求。</p>",
                    },
                ],
            },
            {
                "heading": "将删除的内容",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "您的 Firebase Auth 账户和用户资料",
                            "您拥有的家庭，包括存储在我们云端的库存和位置",
                            "您作为成员所属的其他家庭（将通知该家庭的所有者）",
                            "与您的账户关联的推送通知令牌",
                        ],
                    },
                ],
            },
            {
                "heading": "仅本地使用（无云账户）",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>如果您在未注册账户的情况下使用 "
                            "Larderia，您的数据仅存储在设备上。卸载应用或清除应用存储空间将删除这些数据。您也可以在此之前从<strong>设置</strong>导出备份。</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "更多信息",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>有关我们如何收集和使用数据，请参阅<a href=\"{privacy_url}\">隐私政策</a>。</p>",
                    },
                    {
                        "type": "p",
                        "html": "<p>问题咨询：<a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
        ],
    },
    "zh-Hant":     {
        "html_lang": "zh-Hant",
        "title": "申請刪除帳戶",
        "updated": "最後更新：2026年6月21日",
        "sections": [
            {
                "heading": "在應用程式中刪除（建議）",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>若您已登入雲端帳戶，可在應用程式中永久刪除您的帳戶及相關雲端資料：</p>",
                    },
                    {
                        "type": "ol",
                        "items": [
                            "開啟<strong>設定</strong>",
                            "點按您的個人資料，然後開啟<strong>帳戶</strong>",
                            "點按<strong>刪除帳戶</strong>並以密碼確認",
                        ],
                    },
                    {
                        "type": "p",
                        "html": "<p>刪除立即生效。您將登出，該裝置上的本機應用程式資料將被清除。</p>",
                    },
                ],
            },
            {
                "heading": "透過電子郵件申請刪除",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>若您無法存取應用程式，請從 Larderia 帳戶註冊的地址寄信給我們。我們將驗證所有權並刪除您的帳戶及雲端資料。</p>",
                    },
                    {
                        "type": "p",
                        "html": (
                            "<p><a class=\"cta\""
                            "href=\"mailto:support@cairn-studio.com?subject=Larderia%20account%20deletion%20request\">寄信至 "
                            "support@cairn-studio.com</a></p>"
                        ),
                    },
                    {
                        "type": "p",
                        "html": "<p>請在郵件中包含您註冊的電子郵件地址。我們可能會在處理前要求您確認該申請。</p>",
                    },
                ],
            },
            {
                "heading": "將刪除的內容",
                "blocks": [
                    {
                        "type": "ul",
                        "items": [
                            "您的 Firebase Auth 帳戶和使用者資料",
                            "您擁有的家庭，包括儲存在我們雲端的庫存和位置",
                            "您作為成員所屬的其他家庭（將通知該家庭的所有者）",
                            "與您的帳戶關聯的推播通知權杖",
                        ],
                    },
                ],
            },
            {
                "heading": "僅本機使用（無雲端帳戶）",
                "blocks": [
                    {
                        "type": "p",
                        "html": (
                            "<p>若您在未註冊帳戶的情況下使用 "
                            "Larderia，您的資料僅儲存在裝置上。解除安裝應用程式或清除應用程式儲存空間將刪除這些資料。您也可以在此之前從<strong>設定</strong>匯出備份。</p>"
                        ),
                    },
                ],
            },
            {
                "heading": "更多資訊",
                "blocks": [
                    {
                        "type": "p",
                        "html": "<p>有關我們如何收集和使用資料，請參閱<a href=\"{privacy_url}\">隱私權政策</a>。</p>",
                    },
                    {
                        "type": "p",
                        "html": "<p>問題諮詢：<a href=\"mailto:support@cairn-studio.com\">support@cairn-studio.com</a></p>",
                    },
                ],
            },
        ],
    },
}
