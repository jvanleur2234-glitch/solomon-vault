# Error Recovery

**Learned error handling patterns**

## Git Hub TLS Timeouts
- GitHub occasionally has TLS timeouts
- Commits are local, sync next session
- Track pending syncs in brain/activity_log/

## Service Down
- Check with `service status` or `curl localhost:PORT/health`
- Restart via update_user_service or restart command
- Alert if downtime > 5 minutes

## Claude Rate Limits
- Back off exponentially
- Use NVIDIA Build as fallback
- Switch to Ollama for local tasks

## Docker Failures
- Container paused: use run_sequential_cmds instead of run_bash_command
- Service crash loop: check logs in /dev/shm/

## File Already Exists on Clone
- Use `git pull` instead of clone
- Check if already current with `git status`
