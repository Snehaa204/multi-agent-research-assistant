function updateAgent(id, state){

    const agent =
    document.getElementById(id);

    if(!agent) return;

    agent.classList.remove(
        "waiting",
        "running",
        "completed"
    );

    agent.classList.add(state);
}

function setProgress(percent){

    document.getElementById(
        "progress-fill"
    ).style.width =
    percent + "%";
}

function logActivity(message){

    const activity =
    document.getElementById("activity");

    activity.innerHTML += `
    <div class="activity-line">
        ${message}
    </div>
    `;

    activity.scrollTop =
    activity.scrollHeight;
}

async function runResearch(){

    const topic =
    document.getElementById("topic").value;

    const status =
    document.getElementById("status");

    const report =
    document.getElementById("report");

    if(!topic){

        alert(
            "Enter a research topic"
        );

        return;
    }

    report.innerHTML =
    "Generating report...";

    status.innerHTML =
    "🟡 Running Agents";

    document.querySelectorAll(
        ".agent-step"
    ).forEach(agent=>{
        agent.classList.remove(
            "running",
            "completed"
        );
        agent.classList.add(
            "waiting"
        );
    });

    updateAgent(
        "agent1",
        "running"
    );

    setProgress(10);

    logActivity(
        `🧠 Topic received: ${topic}`
    );

    try{

        const response =
        await fetch(
            "http://127.0.0.1:8000/research",
            {
                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({
                    topic:topic
                })
            }
        );

        const data =
        await response.json();

        if(data.status === "success"){

            updateAgent(
                "agent1",
                "completed"
            );

            updateAgent(
                "agent2",
                "completed"
            );

            updateAgent(
                "agent3",
                "completed"
            );

            updateAgent(
                "agent4",
                "completed"
            );

            updateAgent(
                "agent5",
                "completed"
            );

            updateAgent(
                "agent6",
                "completed"
            );

            updateAgent(
                "agent7",
                "completed"
            );

            setProgress(100);

            status.innerHTML =
            "✅ Research Completed";

            report.innerText =
            data.report;

            logActivity(
                "📚 Papers discovered"
            );

            logActivity(
                "💡 Insights generated"
            );

            logActivity(
                "📝 Report compiled"
            );

        }else{

            status.innerHTML =
            "❌ Error";

            report.innerHTML =
            data.message;
        }

    }catch(error){

        status.innerHTML =
        "❌ Connection Error";

        report.innerHTML =
        error.message;

        logActivity(
            `❌ ${error.message}`
        );
    }
}

document
.getElementById("copyBtn")
.addEventListener("click",()=>{

    navigator.clipboard.writeText(
        document
        .getElementById("report")
        .innerText
    );

    alert(
        "Report Copied!"
    );
});

document
.getElementById("downloadBtn")
.addEventListener("click",()=>{

    const text =
    document
    .getElementById("report")
    .innerText;

    const blob =
    new Blob(
        [text],
        {
            type:"text/plain"
        }
    );

    const link =
    document
    .createElement("a");

    link.href =
    URL.createObjectURL(blob);

    link.download =
    "research_report.txt";

    link.click();
});

document
.getElementById("pdfBtn")
.addEventListener("click",()=>{

    const { jsPDF } =
    window.jspdf;

    const doc =
    new jsPDF();

    const text =
    document
    .getElementById("report")
    .innerText;

    const lines =
    doc.splitTextToSize(
        text,
        180
    );

    doc.text(
        lines,
        10,
        10
    );

    doc.save(
        "research_report.pdf"
    );
});