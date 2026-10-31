# Raccolta YGO

Registro delle tue carte Yu-Gi-Oh! con suggerimenti da nome e codice, rarità, espansione, edizione, lingua, foto, lista dei desideri e controllo doppioni.
È un sito statico: funziona su GitHub Pages senza server.

## Cosa c'è nella cartella

| File | A cosa serve |
|---|---|
| `index.html` | La pagina |
| `cards.json` | Elenco di carte, stampe ed espansioni per i suggerimenti |
| `tools/make_db.py` | Rigenera `cards.json` dai dati pubblici |
| `.github/workflows/update-cards.yml` | Azione che aggiorna `cards.json` ogni lunedì |
| `LICENSE`, `NOTICE.md` | Licenza e fonte dei dati |

## 1. Mettere online il sito

1. Su GitHub crea un repository **pubblico**, per esempio `ygo-raccolta` (Pages sui repository privati richiede un piano a pagamento).
2. Carica i file: **Add file → Upload files** e trascina `index.html`, `cards.json`, `LICENSE`, `NOTICE.md`, `README.md` e la cartella `tools`. Poi **Commit changes**.
3. Crea il file dell'azione a mano, perché le cartelle nascoste a volte non vengono caricate: **Add file → Create new file**, come nome scrivi `.github/workflows/update-cards.yml` (le barre creano le cartelle), incolla il contenuto del file con lo stesso nome e fai **Commit changes**.
4. Vai in **Settings → Pages**. Alla voce *Build and deployment* scegli *Deploy from a branch*, ramo `main`, cartella `/ (root)`, poi **Save**.
5. Dopo uno o due minuti il sito è su `https://TUONOME.github.io/ygo-raccolta/`.

## 2. Aggiornare l'elenco delle carte

L'azione `Aggiorna elenco carte` scarica i dati di [DawnbrandBots/yaml-yugi](https://github.com/DawnbrandBots/yaml-yugi), rigenera `cards.json` e lo salva solo se ci sono novità. Parte da sola ogni lunedì mattina.

- **Provala subito:** scheda **Actions** → *Aggiorna elenco carte* → **Run workflow**. La prima volta dovrebbe dire "Nessuna novità".
- Se l'azione non riesce a salvare, vai in **Settings → Actions → General → Workflow permissions** e scegli *Read and write permissions*.
- GitHub sospende le azioni programmate dopo 60 giorni senza attività nel repository. Se succede, riattivala dalla scheda Actions.
- Nel sito, il pulsante **Aggiorna elenco carte** carica l'ultima versione senza ricaricare la pagina e mostra la data dell'elenco.
- Un set appena uscito può comparire con qualche giorno di ritardo, perché dipende dall'archivio sorgente.

## 3. Usare la raccolta da più dispositivi

Nel sito, in fondo alla pagina, c'è il riquadro **Altri dispositivi**. Collega un secondo repository, **privato**, dove restano raccolta, lista dei desideri e foto.

1. Crea un repository privato, per esempio `ygo-dati`, con l'opzione *Add a README file*.
2. Vai in **Settings (del tuo profilo) → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**. Come accesso scegli *Only select repositories* e solo `ygo-dati`. Nei permessi del repository imposta **Contents: Read and write**. Scegli una scadenza.
3. Nel sito scrivi `tuonome/ygo-dati`, incolla il token e premi **Collega e sincronizza**.
4. Sugli altri dispositivi apri il sito e ripeti il passaggio 3.

Come funziona:
- Ogni modifica parte da sola dopo pochi secondi; **Sincronizza ora** la forza.
- Se due dispositivi cambiano la stessa carta, vince la modifica più recente.
- Il token è salvato solo nel browser di quel dispositivo. Usa un token limitato a `ygo-dati`, così non dà accesso ad altro.
- Senza collegamento i dati restano nel browser, foto comprese. **Esporta CSV** e **Importa CSV** servono per una copia di sicurezza.

## Licenza

`cards.json` deriva da dati con licenza AGPL-3.0 o successive, quindi qui è riportata la stessa licenza. Vedi `NOTICE.md`.
