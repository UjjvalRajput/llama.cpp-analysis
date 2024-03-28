import json

def load_issues_from_json(json_file):
    with open(json_file, 'r') as file:
        issues_data = json.load(file)
    return issues_data

def analyze_size_sufficiency(issues):
    size_concerns_count = 0
    unique_users = set()

    for issue in issues:
        title = issue['title'].lower()
        if 'size' in title or 'footprint' in title or 'memory usage' in title or 'binary size' in title or 'compilation time' in title or 'compile time' in title or 'link time' in title or 'build time' in title:
            size_concerns_count += 1
            unique_users.add(issue['user'])

    total_issues = len(issues)
    total_unique_users = len(unique_users)

    size_analysis = {
        "total_issues": total_issues,
        "size_concerns_count": size_concerns_count,
        "total_unique_users": total_unique_users
    }

    return size_analysis

def analyze_speed_performance(issues):
    speed_concerns_count = 0
    unique_users = set()

    for issue in issues:
        title = issue['title'].lower()
        if 'speed' in title or 'performance' in title or 'GPU performance' in title or 'latency' in title or 'response time' in title or 'bottleneck' in title or 'slowdown' in title or 'lag' in title or 'hang' in title or 'delay' in title or 'responsiveness' in title or 'execution time' in title or 'throughput' in title:
            speed_concerns_count += 1
            unique_users.add(issue['user'])

    total_issues = len(issues)
    total_unique_users = len(unique_users)

    speed_analysis = {
        "total_issues": total_issues,
        "speed_concerns_count": speed_concerns_count,
        "total_unique_users": total_unique_users
    }

    return speed_analysis

def analyze_accuracy_issues(issues):
    accuracy_concerns_count = 0
    unique_users = set()

    for issue in issues:
        title = issue['title'].lower()
        if 'accuracy' in title or 'precision' in title or 'correctness' in title or 'error rate' in title or 'bug' in title or 'wrong result' in title or 'incorrect output' in title or 'mismatch' in title or 'failure output' in title or 'incorrect output' in title or 'inaccurate output' in title or 'imprecise output' in title or 'unreliable output' in title or 'mistake output' in title:
            accuracy_concerns_count += 1
            unique_users.add(issue['user'])

    total_issues = len(issues)
    total_unique_users = len(unique_users)

    accuracy_analysis = {
        "total_issues": total_issues,
        "accuracy_concerns_count": accuracy_concerns_count,
        "total_unique_users": total_unique_users
    }

    return accuracy_analysis


def analyze_issues_by_labels(issues):
    label_counts = {}

    for issue in issues:
        labels = issue.get('labels', [])
        for label in labels:
            if isinstance(label, dict):
                label_name = label['name']
            else:
                label_name = label
            if label_name not in label_counts:
                label_counts[label_name] = {
                    'count': 0,
                    'users': set()
                }
            label_counts[label_name]['count'] += 1
            label_counts[label_name]['users'].add(issue['user'])

    label_analysis = []
    for label, info in label_counts.items():
        label_info = {
            "label": label,
            "count": info['count'],
            "unique_users": len(list(info['users']))
        }
        label_analysis.append(label_info)

    return label_analysis


def main():
    json_file = "issues.json"
    issues = load_issues_from_json(json_file)
    if issues:
        size_analysis = analyze_size_sufficiency(issues)
        speed_analysis = analyze_speed_performance(issues)
        accuracy_analysis = analyze_accuracy_issues(issues)
        label_analysis = analyze_issues_by_labels(issues)

        analysis_results = {
            "size_sufficiency": size_analysis,
            "speed_performance": speed_analysis,
            "accuracy_issues": accuracy_analysis,
            "label_analysis": label_analysis
        }

        with open("analysis_results.json", "w") as output_file:
            json.dump(analysis_results, output_file, indent=4)
    else:
        print("Failed to load issues from JSON file.")

if __name__ == "__main__":
    main()
